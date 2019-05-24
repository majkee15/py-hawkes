import os
import sys
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np
from Cython.Build import cythonize

"""
The module uses Eigen C++ library and therefore
setup.py needs to be able to locate it.
Change the last directory in include_dirs
for your local directory containing Eigen
header files.
"""

cur_dir = os.path.dirname(os.path.realpath(__file__))
lib_dir = os.path.join(cur_dir, r'lib')
os.chdir(cur_dir)

sourcefiles = [r"pyhawkes.pyx", os.path.join(lib_dir,"exp_hawkes.cpp"),
               os.path.join(lib_dir,"power_hawkes.cpp"), os.path.join(lib_dir, "general_hawkes.cpp"), os.path.join(lib_dir,r"additional_functions.cpp")]

setup(cmdclass={'build_ext': build_ext},
      ext_modules=[Extension("pyhawkes", sourcefiles, language="c++",
                             include_dirs=[".", np.get_include(), lib_dir,
                                           r"/usr/local/Cellar/eigen/3.3.7/include/eigen3"], extra_compile_args=["-std=c++11"])])

