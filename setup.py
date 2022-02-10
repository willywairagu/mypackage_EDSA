from setuptools import setup, find_packages

setup(
    name="mypackage",
    version='',
    packages=find_packages(exclude=['tests*']),
    licens='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<username>/<package>',
    author='Wairagu Wilberforce Wahome',
    author_email='wairaguwilberforce99@gmail.com'

)