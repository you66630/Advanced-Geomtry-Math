

from setuptools import setup, find_packages

classifiers = [
    'Devolpment Status :: 1 - Production/Stable',
    'Intended Audience :: Everyone',
    'Operating System :: Mirosoft :: Windows :: WIndows 10 , 11',
    'License :: OSI Approved :: MIT Licence',
    'Programing Language :: Python :: 3'
]

setup( 
    name='MGA',
    version='0.0.1',
    description='A simple Python library for More Methods For Math .',
    long_description=open('README.md').read() + '\n\n' + open('ChANGELOG.txt').read(),
    author='Youssef Ahmed',
    author_email='youssefahmedmoawedhamied@gmail.com',
    License='MIT',
    classifiers=classifiers,
    keywords='More-Methods',
    packages=find_packages(),
)