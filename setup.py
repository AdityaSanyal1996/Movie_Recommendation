import setuptools

with open("README.md", "r", encoding = "utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Movie_Recommendation"
AUTHOR_USER_NAME = "AdityaSanyal1996"
SRC_REPO = "recommender"
AUTHOR_EMAIL = "adityasanyal1996@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "a python package for a movie recommendation system",
    long_description = long_description,
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir = {"" : "src"},
    packages = setuptools.find_packages(where="src")

)