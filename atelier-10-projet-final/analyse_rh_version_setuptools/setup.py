from setuptools import setup, find_packages

setup(
    name='analyse_employes',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
        'seaborn',
        'fpdf',
        'openpyxl'
    ],
)
