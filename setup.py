import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="nhcarrigan",
    version="0.1",
    description="Just so that you could do pip install nhcarrigan",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Vyvy-vi/nhcarrigan",
    author="Vyvy-vi",
    author_email="vyom.j@pm.me",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["nhcarrigan"],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "realpython=nhcarrigan.__main__:main",
        ]
    },
)
