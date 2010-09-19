
import numpy as np
cimport numpy as np


cdef extern from "acml_mv.h":
    int vrda_exp(int n, double a[], double y[])


def vdexp(np.ndarray[np.float64_t] arr):
    cdef np.ndarray[np.float64_t] out = np.empty_like(arr)
    cdef int n = arr.shape[0]

    vrda_exp(n, <double*>arr.data, <double*>out.data)
    return out
