from setuptools import setup, find_packages

setup(
    name="ecomer",
    description = "Python client for Ecomer API",
    version='0.1.1',
    url="https://github.com/gwenlake/ecomer-python",
    author="The Ecomer Team",
    author_email="info@gwenlake.com",
    install_requires=["requests", "pydantic", "numpy", "pandas", "tenacity", "shapely", "geopandas"],
    packages=find_packages(exclude=('tests'))
)
