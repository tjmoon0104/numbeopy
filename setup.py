from setuptools import setup, find_packages

NAME = "numbeopy"
VERSION = "0.0.1"
DESCRIPTION = "Numbeo API Python Package"
LONG_DESCRIPTION = "Use Numbeo API on Python"

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name=NAME,
    version=VERSION,
    author="Taejun Moon",
    author_email="tjmoon0104@outlook.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        "requests>=2.27.1",
        "iso3166>=2.0.2"
    ],  # add any additional packages that

    keywords=['python', 'numbeo'],
    classifiers=[
        "Programming Language :: Python :: 3",
    ]
)
