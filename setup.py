from setuptools import setup, find_packages
import os

here = os.path.dirname(os.path.realpath(__file__))


def get_install_requires():
    with open(os.path.join(here, 'requirements.txt'), 'r') as f:
        return f.read().splitlines()


def get_version():
    with open(os.path.join(here, 'version.txt'), 'r') as f:
        return f.readline().split()[0]  # Filter out other junk


setup(
    name='yoyo',
    version=get_version(),
    url='https://github.com/eL0ck/aws-build',
    author='eL0ck',
    author_email='tpj800@gmail.com',
    license='Apache',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, <4',
    packages=find_packages(),
    install_requires=get_install_requires(),
    entry_points={
        'console_scripts': [
            'yoyo=yoyo.flojo:dickhead',
        ],
    },
    data_files=[
        'version.txt',
        'requirements.txt',
    ],
    zip_safe=False,
)
