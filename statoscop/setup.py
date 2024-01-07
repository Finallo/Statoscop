from setuptools import setup, find_packages

setup(
    name="Statoscop",
    version="1.2.1",
    author="Finallo",
    author_email="finallo360@gmail.com",
    description="A package to have data of Valorant esport. (League and TFT are coming)",
    packages=find_packages(),
    keywords='Valorant Stats',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)