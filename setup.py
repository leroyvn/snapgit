from setuptools import setup, find_packages


setup(
    name="snapgit",
    version="1.0.0",
    author="Vincent Leroy",
    author_email="vincent.leroy@rayference.eu",
    description="",
    long_description="",

    install_requires=[
        "click>=5.0",
    ],
    entry_points={
        "console_scripts": [
            "snapgit=snapgit:main",
        ],
    },
    packages=find_packages(),
)
