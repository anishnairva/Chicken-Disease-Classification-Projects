"""
This file is the setup script for the package.
"""

# Import the setuptools module
import setuptools

# Open the README.md file in read mode and store its content in the long_description variable
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Define the version number of the package
__version__ = "0.0.0"

# Define the repository name, author username, source repository name, author email
REPO_NAME = "Chicken-Disease-Classification-Projects"
AUTHOR_USER_NAME = "anishnairva"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "anishnairva@gmail.com"

# Call the setuptools.setup function with the necessary information for the package
setuptools.setup(
    name=SRC_REPO, # The name of the package
    version=__version__, # The version number of the package
    author=AUTHOR_USER_NAME, # The username of the author
    author_email=AUTHOR_EMAIL, # The email address of the author
    description="A small python package for CNN app", # A short description of the package
    long_description=long_description, # The long description of the package, read from the README.md file
    long_description_content="text/markdown", # The format of the long description
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}", # The URL of the repository
    project_urls={ # A dictionary of project URLs
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues", # The URL of the bug tracker
    },
    package_dir={"": "src"}, # A dictionary specifying the package directories
    packages=setuptools.find_packages(where="src") # A list of packages found in the src directory
)