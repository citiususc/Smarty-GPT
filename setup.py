#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages
import smartygpt

setup(
    name='smarty-gpt',
    version=smartygpt.__version__,
    description=(
        'A wrapper of LLMs that biases its behaviour using prompts and contexts in a transparent manner to the end-users'
    ),
    url='https://github.com/citiususc/Smarty-GPT',
    author='Marcos Fernández-Pichel',
    author_email='marcosfernandez.pichel@usc.es',
    license='Apache License (Version 3.0)',
    packages=find_packages(),
    zip_safe=False,
    python_requires=">=3.6",
    install_requires=[
        'openai',
        'argparse',
        'multiprocess==0.70.13',
        'datasets',
        'nltk',
        'requests',
        'transformers==4.20.1',
        'huggingface_hub==0.7.0',
        'configparser'
    ])