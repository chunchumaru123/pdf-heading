from setuptools import setup, find_packages
import codecs
import os

VERSION = '2.0.2'
DESCRIPTION = 'PDF subheadings finder with text.A package that allows to find subheadings in a PDF.'
# Setting up
setup(
    name="easypdfheading",
    version=VERSION,
    author="VasanthKumar",
    author_email="<vasanthtjr@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['pdfminer.six','fitz','pandas','PyMuPDF'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)