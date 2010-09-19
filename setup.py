#!/usr/bin/env python

from sys import argv
from distutils.core import setup, Extension
from Cython.Distutils import build_ext

import numpy as np

##############################################################################


if __name__ == "__main__":

    acml_dir='/opt/acml-4.4.0/gfortran64/'
    #acml_dir='/cm/shared/apps/acml/4.3.0/gfortran64/'

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

