from setuptools import setup, find_packages
import stodle

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open('README.md') as f:
    long_description = f.read()

setup(
    name='stodle',
    version='0.0.1',
    long_description=long_description,
    packages=find_packages(),
    url='https://github.com/WaylonWalker/stodle',
    license='MIT',
    author='Waylon Walker',
    author_email='quadmx08@gmail.com',
    description='Stop Idle for windows',
    install_requires=required,
)
