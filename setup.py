from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='opensubz',
    version='0.1.2',
    description='Easily search opensubtitles subtitles',
    long_description=long_description,
    url='https://github.com/danielfsousa/opensubz',
    download_url='https://github.com/danielfsousa/opensubz/archive/0.1.3.tar.gz',
    author='Daniel Sousa',
    author_email='sousa.dfs@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Multimedia',
        'Environment :: Win32 (MS Windows)',
        'Operating System :: Microsoft :: Windows',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='script download subtitles opensubtitles',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['requests'],
    data_files=[
        ('icon', ['icon/play.ico']),
        ('config', ['config/opensubz.ini'])
    ],
    entry_points={
        'console_scripts': [
            'opensubz=bin.opensubz:main',
        ],
    },
)