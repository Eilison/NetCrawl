# coding: utf-8

from setuptools import setup, find_packages

setup(
    name='netcrawl',
    version='v1.2.1',
    author='eilison',
    author_email='1277886419@qq.com',
    url='https://github.com/Eilison/NetCrawl.git',
    description=u'support ',
    license='MIT License',
    packages=find_packages(),
    platforms=["all"],
    install_requires=[
        "selenium"
    ]
)