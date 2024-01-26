from setuptools import setup, find_packages

setup(
    name='sudoku_solver',
    version='0.1.0',
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "numpy>=1.26.1",
        "pandas>=2.1.2"
    ],
    author='Alejandro Arias',
    author_email='jandroariass@gmail.com',
    description='Sudoku solver',
    url='https://github.com/Alexarr6/sudoku-solver',
)
