from distutils.core import setup

setup(
    description="Recon.gg",
    author="Finallo",
    author_email="finallo360@gmail.com",
    name="Recon.GG",
    packages=["recongg"],
    url="recongg.gg",
    version="0.1.0",
    entry_points={
        "console_scripts":
            ["recongg = recongg.app:main"]
    }
)