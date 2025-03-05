from setuptools import setup, find_packages

setup(
    name="leetcode-cli",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "gql",
        "requests",
        "requests_toolbelt",
        "argcomplete"
    ],
    entry_points={
        "console_scripts": [
            "leet=leet.__main__:parse_args"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console"
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.7',
)
