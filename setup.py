from setuptools import setup, find_packages

setup(
    name='docker-optimizer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'docker',
        'requests',
        'fpdf',
        'typing',
        'csv',
        'json',
    ],
    entry_points={
        'console_scripts': [
            'docker-optimizer=docker_optimizer:main',
        ],
    },
)