from setuptools import setup, find_packages

setup(
    name='your_project_name',
    version='0.1',
    packages=find_packages(),
    python_requires='>=3.12.0,<4.0',
    install_requires=[
        'numpy==1.26.4',
        'keras==3.6.0',
        'music21==9.1.0',
        'tensorflow==2.17.0',
    ],
)