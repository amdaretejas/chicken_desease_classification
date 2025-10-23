import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "chicken_desease_classification"
AUTHER_USER_NAME = "Tejas Amdare"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "amdaretejas1@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHER_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://gihub.com/{AUTHER_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://gihub.com/{AUTHER_USER_NAME}/{REPO_NAME}/issue",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)