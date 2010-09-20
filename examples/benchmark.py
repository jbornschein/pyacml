#!/usr/bin/env python

from __future__ import division

import sys
sys.path.append("../")

from timeit import timeit

import numpy as np
import pyacml


if __name__ == "__main__":
    ufuncs64 = [
        ("sin"  , "np.sin(a)"  , "pyacml.sin(a)"  ),
        ("cos"  , "np.cos(a)"  , "pyacml.cos(a)"  ),
        ("exp"  , "np.exp(a)"  , "pyacml.exp(a)"  ),
        ("log"  , "np.log(a)"  , "pyacml.log(a)"  ),
        ("log2" , "np.log2(a)" , "pyacml.log2(a)" ),
        ("log10", "np.log10(a)", "pyacml.log10(a)"),
    ]
   

    print 
    print " Running function on vector of size 1,000,000...."
    print
    print "   Function | NumPy time| ACML time | Speedup "
    print "------------+-----------+-----------+---------"

    setup = "import numpy as np; import pyacml; a = np.linspace(0, 100, 1000000)"
    for name, np_func, acml_func in ufuncs64:
        t_np = timeit(np_func, setup=setup, number=10)
        t_acml = timeit(acml_func, setup=setup, number=10)

        print " %10s | %6.2f ms | %6.2f ms |    %3.1f " % (name, t_np*1000, t_acml*1000, t_np/t_acml)

    print
