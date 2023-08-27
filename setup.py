import setuptools


#reading the description from the readme file on the github
with open("README.md","r",encoding="utf-8") as f :
    long_description = f.read()
    
    
__version__="0.0.0"
REPO_NAME = "mlops_end_to_end_project"
AUTHOR_USER_NAME = "ronakjpatel"
SRC_REPO = "end_to_end_mlops"
AUTHOR_EMAIL = "rjpatel7991@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A personal project for learning mlops",
    long_description=long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)