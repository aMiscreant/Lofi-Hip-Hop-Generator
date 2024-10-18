from setuptools import setup, find_packages

setup(
    name='your_project_name',
    version='0.1',
    packages=find_packages(),
    python_requires='>=3.12.0,<4.0',
    install_requires=[
        'numpy==1.24.0',
        'keras==2.11.0',
        'music21==6.1.0',
    ],
)