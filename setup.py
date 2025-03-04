from setuptools import setup, find_packages

setup(
    name="leet",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "gql==3.5.1",
        "requests==2.32.3",
        "requests_toolbelt==1.0.0",
        "argcomplete==3.2.2"
    ],
    entry_points={
        "console_scripts": [
            "leet=leet.__main__:parse_args"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Linux",
    ],
    python_requires='>=3.6',
)
