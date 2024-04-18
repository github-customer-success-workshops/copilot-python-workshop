from setuptools import setup, find_packages

setup(
    name='copilot-python-workshop',
    version='0.0.1',
    description='Copilot Worshop in Python',
    author='bxtp4p',
    author_email='bxtp4p@github.com',
    packages=find_packages('app'),
    package_dir={'': 'app'},
    install_requires=[
        # Add your project dependencies here
    ],
)