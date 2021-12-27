import os
from distutils.core import setup
from setuptools import find_packages
from promote import version

setup(
    name="promote",
    version=version.__version__,
    author="Alteryx",
    author_email="promotedev@alteryx.com",
    url="https://github.com/alteryx/promote-python-client",
    packages=find_packages(),
    description="Client for deploying Python models to Promote.",
    license="BSD",
    classifiers=(
    ),
    long_description=open("README.rst").read(),
    keywords=['alteryx', 'scikit-learn', 'numpy', 'pandas'],
)
