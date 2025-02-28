from leet.api.html2text import html2text
import re
import sys
import requests
import json

class AlfaAPIClient:
    BASE_API: str = "https://alfa-leetcode-api.onrender.com/"
    TITLE_SLUG_PATTERN: re.Pattern = re.compile(r"[a-z0-9]+\-")

    @staticmethod
    def request(request: str, **params):
        params_str = ('?' if params else '') + "&".join([f"{k}={v}" for k, v in params.items()])
        with requests.get(f"{AlfaAPIClient.BASE_API}{request}{params_str}") as response:
            return response.json()

    @staticmethod
    def slug_from_input(user_input: str, recur: bool = False) -> str:
        if AlfaAPIClient.TITLE_SLUG_PATTERN.match(user_input):
            # might already be a slug
            question_data = AlfaAPIClient.request("select", titleSlug=user_input)
            if question_data != {}:
                return user_input
        
        elif re.match(r"[0-9]+", user_input):
            # might be the question number
            try:
                problem_number = int(user_input)

                if problem_number >= 0:
                    problem_data = AlfaAPIClient.request("problems", skip=problem_number - 1, limit=1)
                    if problem_data["count"] > 0:
                        return problem_data["problemsetQuestionList"][0]["titleSlug"]
            except Exception as e:
                ...
        
        else:
            if recur:
                raise KeyError(user_input)
            
            # might be the title
            fmt_user_input = user_input.replace(' ', '-').lower()
            
            return AlfaAPIClient.slug_from_input(fmt_user_input, recur=True)

    @staticmethod
    def get_question(slug):
        slug = AlfaAPIClient.slug_from_input(slug)
        return AlfaAPIClient.request("select", titleSlug=slug)
    

if __name__ == "__main__":
    question_details = AlfaAPIClient.get_question(" ".join(sys.argv[1:]))
    question = question_details["question"]
    question_text = html2text(question)
    question_text = question_details["link"] + "\n\n" + question_text
    print(question_text)
