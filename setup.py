import os

from setuptools import setup, find_packages
from setuptools.command.install import install
from functools import reduce


class PostInstall(install):
    def __init__(self, *args, **kwargs):
        super(PostInstall, self).__init__(*args, **kwargs)
        _install_requirements()


def _install_requirements():
    os.system("pre-commit install")


REQUIRED_PACKAGES = [
    "Flask-PyMongo == 2.3.0",
    "pydantic == 1.10.2",
    "pymongo == 4.3.2",
]

EXTRA_REQUIREMENTS = {}

name = "skip-db-lib"
version = "1.0.0"
description = ("A modular library that exposes a set of database operation")

setup(
    name=name,
    version=version,
    description=description,
    python_requires=">=3.8",
    packages=[],#["res", *find_packages(include=["hemunah_core*"])],
    package_data={"": ["res/*.csv", "res/*.json", "res/*.yaml"]},
    include_package_data=True,
    install_requires=REQUIRED_PACKAGES,
    extras_require={
        **EXTRA_REQUIREMENTS,
        "all": reduce(lambda agg, value: agg + value, EXTRA_REQUIREMENTS.values(), []),
    },
    cmdclass={"install": PostInstall},
)
