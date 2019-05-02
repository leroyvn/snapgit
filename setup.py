from setuptools import setup, find_packages


setup(
    name="snapgit",
    version="2.0.0",
    author="Vincent Leroy",
    author_email="vincent.leroy@rayference.eu",
    description="",
    long_description="",

    install_requires=[
        "click>=5.0",
        "pyyaml>=5.1"
    ],
    entry_points={
        "console_scripts": [
            "snapgit=snapgit:main",
        ],
    },
    packages=find_packages(),
)
