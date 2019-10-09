from setuptools import setup

setup(
    name='my_hello_lucas_astur',
    version='0.1',
    packages=['my_hello'],
    install_requires=[
        'gitpython', 
    ],
    scripts=['scripts/hello.py']
)