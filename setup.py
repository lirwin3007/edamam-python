import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="edamam_api",
    version="0.0.1",
    author="Louis Irwin",
    author_email="coding@louisirwin.co.uk",
    description="Python library to interface with the edamam API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lirwin3007/edamam-python",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ),
)
