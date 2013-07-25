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
            self.assertEqual(arr.shape, out.shape, msg="Failed for %s" % acml_func)

    def test_2d_shape(self):
        arr = np.linspace(1, 10, 100).reshape( (10, 10) )
        for np_func, acml_func in self.vector_funcs:
            out = acml_func(arr)
            self.assertEqual(arr.shape, out.shape, msg="Failed for %s" % acml_func)

    def test_allclose(self):
        arr = np.linspace(0, 100, 1000)
        for np_func, acml_func in self.vector_funcs:
            np_out = np_func(arr)
            acml_out = acml_func(arr)
            self.assertTrue( np.allclose(np_out, acml_out), msg="Failed for %s" % acml_func)

    def test_nan(self):
        arr =np.empty(100)
        arr[:] = np.nan
        for np_func, acml_func in self.vector_funcs:
            np_out = np_func(arr)
            acml_out = acml_func(arr)

            equal_nan = np.isnan(np_out) == np.isnan(acml_out)
            equal_posinf = np.isposinf(np_out) == np.isposinf(acml_out)
            equal_neginf = np.isneginf(np_out) == np.isneginf(acml_out)
            self.assertTrue( np.alltrue(equal_nan), msg="NaN-test failed for %s" % acml_func)
            self.assertTrue( np.alltrue(equal_posinf), msg="posinf-test failed for %s" % acml_func)
            self.assertTrue( np.alltrue(equal_neginf), msg="neginf-test failed for %s" % acml_func)

    def test_posinf(self):
        arr =np.empty(100)
        arr[:] = np.inf
        for np_func, acml_func in self.vector_funcs:
            np_out = np_func(arr)
            acml_out = acml_func(arr)

            equal_nan = np.isnan(np_out) == np.isnan(acml_out)
            equal_posinf = np.isposinf(np_out) == np.isposinf(acml_out)
            equal_neginf = np.isneginf(np_out) == np.isneginf(acml_out)
            self.assertTrue( np.alltrue(equal_nan), msg="NaN-test failed for %s" % acml_func)
            self.assertTrue( np.alltrue(equal_posinf), msg="posinf-test failed for %s" % acml_func)
            self.assertTrue( np.alltrue(equal_neginf), msg="neginf-test failed for %s" % acml_func)

    def test_neginf(self):
        arr =np.empty(100)
        arr[:] = -np.inf
        for np_func, acml_func in self.vector_funcs:
            np_out = np_func(arr)
            acml_out = acml_func(arr)

            equal_nan = np.isnan(np_out) == np.isnan(acml_out)
            equal_posinf = np.isposinf(np_out) == np.isposinf(acml_out)
            equal_neginf = np.isneginf(np_out) == np.isneginf(acml_out)
            self.assertTrue( np.alltrue(equal_nan), msg="NaN-test failed for %s" % acml_func)
            self.assertTrue( np.alltrue(equal_posinf), msg="posinf-test failed for %s" % acml_func)
            self.assertTrue( np.alltrue(equal_neginf), msg="neginf-test failed for %s" % acml_func)


if __name__ == "__main__":
    unittest.main()

