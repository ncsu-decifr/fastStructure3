from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

# Define all individual extensions
ext_modules = [
    # Utility module
    Extension(
        "utils",
        sources=["utils.pyx"],
        include_dirs=[numpy.get_include(), '.']
    ),
    # Variable update modules
    Extension(
        "admixprop",
        sources=["admixprop.pyx", "C_admixprop.c"],
        include_dirs=[numpy.get_include(), '.']
    ),
    Extension(
        "allelefreq",
        sources=["allelefreq.pyx", "C_allelefreq.c"],
        libraries=["gsl", "gslcblas"],
        extra_compile_args=["-O3"],
        include_dirs=[numpy.get_include(), '.']
    ),
    Extension(
        "marglikehood",
        sources=["marglikehood.pyx", "C_marglikehood.c"],
        include_dirs=[numpy.get_include(), '.']
    )
]

# Run setup exactly once for the entire project
setup(
    name='fastStructure_vars',
    author='Anil Raj',
    version='1.0',
    author_email='rajanil@stanford.edu',
    # cythonize compiles all .pyx files at once
    ext_modules=cythonize(ext_modules, language_level="3")
)
