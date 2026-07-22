from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

ext_modules = [
    # Main project modules (located in root)
    Extension("parse_bed", ["parse_bed.pyx"], include_dirs=[numpy.get_include(), '.']),
    Extension("parse_str", ["parse_str.pyx"], include_dirs=[numpy.get_include(), '.']),
    Extension("fastStructure", ["fastStructure.pyx"], include_dirs=[numpy.get_include(), '.', 'vars/']),

    # Utility module (fixed to point to vars/)
    Extension("utils", sources=["vars/utils.pyx"], include_dirs=[numpy.get_include(), '.', 'vars/']),

    # Variable update modules (located in vars/)
    Extension("admixprop", sources=["vars/admixprop.pyx", "vars/C_admixprop.c"], include_dirs=[numpy.get_include(), '.', 'vars/']),
    Extension("allelefreq", sources=["vars/allelefreq.pyx", "vars/C_allelefreq.c"],
              libraries=["gsl", "gslcblas"],
              extra_compile_args=["-O3"],
              include_dirs=[numpy.get_include(), '.', 'vars/']),
    Extension("marglikehood", sources=["vars/marglikehood.pyx", "vars/C_marglikehood.c"], include_dirs=[numpy.get_include(), '.', 'vars/'])
]

setup(
    name='fastStructure_package',
    author='Anil Raj',
    version='1.0',
    ext_modules=cythonize(ext_modules, language_level="3", include_path=["vars"])
)
