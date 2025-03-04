import re
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from graphql import DocumentNode

question_title_query = gql("""
query questionTitle($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    title
    titleSlug
    isPaidOnly
    difficulty
    likes
    dislikes
  }
}""")

question_content_query = gql("""
query questionContent($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    content
    mysqlSchemas
  }
}
""")

problem_question_query = gql("""
query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
  problemsetQuestionList: questionList(
    categorySlug: $categorySlug
    limit: $limit
    skip: $skip
    filters: $filters
  ) {
    total: totalNum
    questions: data {
      acRate
      difficulty
      freqBar
      frontendQuestionId: questionFrontendId
      isFavor
      paidOnly: isPaidOnly
      status
      title
      titleSlug
      topicTags {
        name
        id
        slug
      }
      hasSolution
      hasVideoSolution
    }
  }
}
""")

class GraphQLClient:
    BASE_API: str = "https://leetcode.com/graphql/"
    TITLE_SLUG_PATTERN: re.Pattern = re.compile(r"[a-z0-9]+\-")
    
    def __init__(self):
        self.transport = RequestsHTTPTransport(
            url=self.BASE_API,
            use_json=True,
            verify=True,
            retries=3  # Retry in case of temporary issues
        )
        self.client = Client(transport=self.transport, fetch_schema_from_transport=False)

    def request(self, query: DocumentNode, **params) -> dict:
        try:
            result = self.client.execute(document=query, variable_values=params)
            return result
        except Exception as e:
            print(e)
            raise e

    def slug_from_input(self, user_input: str, recur: bool = False) -> str:
        if GraphQLClient.TITLE_SLUG_PATTERN.match(user_input):
            # might already be a slug
            question_data = self.request(question_title_query, titleSlug=user_input)
            if question_data != {}:
                return user_input
        
        elif re.match(r"[0-9]+", user_input):
            # might be the question number
            try:
                problem_number = int(user_input)

                if problem_number >= 0:
                    problem_data = self.request(problem_question_query, skip=problem_number - 1, limit=1, filters={}, categorySlug="")
                    if problem_data["problemsetQuestionList"]["total"] > 0:
                        return problem_data["problemsetQuestionList"]["questions"][0]["titleSlug"]
            except Exception as e:
                ...
        
        else:
            if recur:
                raise KeyError(user_input)
            
            # might be the title
            fmt_user_input = user_input.replace(' ', '-').lower()
            
            return self.slug_from_input(fmt_user_input, recur=True)

    def get_question(self, slug: str) -> dict:
        slug = self.slug_from_input(slug)

        question_info = self.request(question_title_query, titleSlug=slug)
        question_text = self.request(question_content_query, titleSlug=slug)
        
        question_info["question"]["content"] = question_text["question"]["content"]
        
        return question_info["question"]
        

    def get_problem_amount(self):
        problem_data = self.request(problem_question_query, skip=0, limit=1, filters={}, categorySlug="")
        return problem_data["problemsetQuestionList"]["total"]
