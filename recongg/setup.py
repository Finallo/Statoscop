from setuptools import setup, find_packages

setup(
    name="recongg",
    version="1.0.0",
    author="Finallo",
    author_email="finallo360@gmail.com",
    description="A package to have data of Valorant esport.",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)