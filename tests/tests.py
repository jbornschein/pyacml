#!/usr/bin/env python

import sys
sys.path.insert(0, "../")

import numpy as np
import unittest

import pyacml


class TestVectorFuncs(unittest.TestCase):
    vector_funcs = (
        (np.sin,   pyacml.sin), 
        (np.cos,   pyacml.cos),
        (np.exp,   pyacml.exp),
        (np.log,   pyacml.log),
        (np.log2,  pyacml.log2),
        (np.log10, pyacml.log10),
    )

    def test_1d_shape(self):
        arr = np.linspace(1, 10, 100)
        for np_func, acml_func in self.vector_funcs:
            out = acml_func(arr)
            self.assertEqual(arr.shape, out.shape)

    def test_2d_shape(self):
        arr = np.linspace(1, 10, 100).reshape( (10, 10) )
        for np_func, acml_func in self.vector_funcs:
            out = acml_func(arr)
            self.assertEqual(arr.shape, out.shape)

    def test_result(self):
        arr = np.linspace(1, 100, 1000)
        for np_func, acml_func in self.vector_funcs:
            np_out = np_func(arr)
            acml_out = acml_func(arr)
            self.assertTrue( np.allclose(np_out, acml_out) )

            

if __name__ == "__main__":
    unittest.main()

