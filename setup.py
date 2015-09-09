import os
from setuptools import setup, find_packages


def read_file(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    return open(filepath, 'r').read()

setup(
    name='junebug',
    version='0.0.3a',
    url='http://github.com/praekelt/junebug',
    license='BSD',
    description=(
        'A system for managing text messaging transports via a RESTful HTTP ',
        'interface'),
    long_description=read_file('README.rst'),
    author='Praekelt Foundation',
    author_email='dev@praekeltfoundation.org',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'klein',
        'jsonschema',
        'treq',
        'vumi',
    ],
    entry_points='''
    [console_scripts]
    jb = junebug.command_line:main
    ''',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
