from setuptools import setup

setup(
    name='alethtils',
    url='https://github.com/JamesRCr/Alethtils',
    author='James Ronald Crowley',
    email='j.crowely@mail.utoronto.ca',
    packages=['alethtils'],
    install_requirements=['logging',
                          'functools',
                          'timeit'],
    version='0.1',
    license='MIT',
    description='A basic utility package for simple performance testing.',
    long_description=open('README.md').read()
)
