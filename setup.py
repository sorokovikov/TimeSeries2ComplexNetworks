from setuptools import setup, find_packages

with open('README.md', mode='r', encoding='utf-8') as readme:
    LONG_DESCRIPTION = readme.read()

setup(
    name='time_series2complex_networks',
    version='0.1',
    packages=find_packages(),
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    install_requires=[
        'matplotlib==3.3.0',
        'pandas==1.0.5',
        'networkx==2.4'
    ]
)
