from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.9'
DESCRIPTION = 'To be deleted later'
LONG_DESCRIPTION = 'Dummy package to test direct publishing from GitHub to PyPi'

# Setting up
setup(
    name="dummypypi2",
    version=VERSION,
    author="Bart Wolleswinkel",
    author_email="b.wolleswinkel@tudelft.nl",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['numpy'],
    keywords=['python', 'dummy', 'github', 'pypi', 'test'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
