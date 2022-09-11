from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in operation_unit/__init__.py
from operation_unit import __version__ as version

setup(
	name="operation_unit",
	version=version,
	description="An operating unit (OU) is an organizational entity part of a company",
	author="Zamiltec",
	author_email="hello@zamiltec.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
