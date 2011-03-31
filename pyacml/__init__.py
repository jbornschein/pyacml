"""
  Python wrapper for the AMD Math Library


Provides high performance primitives for nummerical computing.
"""

import numpy as np

import vm


def call_vec_func(arr, out, func):
    orig_shape = arr.shape
    if not arr.flags.c_contiguous:
        arr = arr.flatten()
    arr = arr.reshape(-1)

    # Create result array (if neccessary)
    if out is None:
        out = np.empty_like(arr)

    # Call acual ACML function
    func(arr.size, arr, out)

    return out.reshape(orig_shape)

def sin(arr, out=None):
    return call_vec_func(arr, out, vm.sin)

def cos(arr, out=None):
    return call_vec_func(arr, out, vm.cos)

def exp(arr, out=None):
    return call_vec_func(arr, out, vm.exp)

def exp(arr, out=None):
    return call_vec_func(arr, out, vm.exp)

def log(arr, out=None):
    return call_vec_func(arr, out, vm.log)

def log2(arr, out=None):
    return call_vec_func(arr, out, vm.log2)

def log10(arr, out=None):
    return call_vec_func(arr, out, vm.log10)

