from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='time_series2complex_networks',
    version='0.1',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    install_requires=[
        'matplotlib==3.3.0',
        'pandas==1.0.5',
        'networkx==2.4'
    ]
)
