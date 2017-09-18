from setuptools import setup
from setuptools import find_packages

import zinnia_ajax as package

setup(
    name='zinnia_ajax',
    version=package.__version__,
    description='An extension for AJAX browsing of '
                'Django Blog Zinnia',
    long_description='\n'.join([open('README.rst').read()]),
    keywords='django, blog, weblog, zinnia, ajax',

    author=package.__author__,
    author_email=package.__email__,
    url=package.__url__,

    packages=find_packages(),

    include_package_data=True,
    install_requires=[]
)
