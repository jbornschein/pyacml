#!/usr/bin/env python

from sys import argv
from os import environ
from distutils.core import setup, Extension
from Cython.Distutils import build_ext

import numpy as np

#============================================================================
# Main

def find_acml():
    if 'ACML_PATH' in environ:
        acml_dir=environ['ACML_PATH']
    else:
        print "Warning: ACML_PATH environment variable not found. Assuming installation in /opt/acml/"
        acml_dir='/opt/acml/'            # default 
    return acml_dir

#============================================================================
# Main

if __name__ == "__main__":

    # ACML installation path:
    acml_dir=find_acml()
    numpy_dir=np.get_include()

    include_dirs=[acml_dir+'/include', numpy_dir]
    library_dirs=[acml_dir+'/lib/']
    libraries=['acml', 'acml_mv']

    ext_modules=[
        Extension("pyacml.vm", ["pyacml/vm.pyx"], 
                  include_dirs=include_dirs,
                  library_dirs=library_dirs, libraries=libraries) 
    ]

    setup(
        name='pyacml',
        version='0.1',
        description='ACML Python Wrapper',
        author='Bernstein Vision Initiative Frankfurt',
        author_email='bernstein@fias.uni-frankfurt.de',
        license='TBD',
        cmdclass = {'build_ext': build_ext},
        ext_modules = ext_modules,
        packages=[
            'pyacml'
        ],
    )

