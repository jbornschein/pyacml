
import numpy as np
cimport numpy as np

# ACML vector  functions 
cdef extern from "acml_mv.h":
    int vrda_sin(int n, double a[], double y[])
    int vrda_cos(int n, double a[], double y[])
    int vrda_exp(int n, double a[], double y[])
    int vrda_log(int n, double a[], double y[])
    int vrda_log10(int n, double a[], double y[])
    int vrda_log2(int n, double a[], double y[])


##############################################################################
# Function wrappers

def sin(np.ndarray[np.float64_t] arr):
    cdef np.ndarray[np.float64_t] out = np.empty_like(arr)
    cdef int n = arr.shape[0]

    vrda_sin(n, <double*>arr.data, <double*>out.data)
    return out

def cos(np.ndarray[np.float64_t] arr):
    cdef np.ndarray[np.float64_t] out = np.empty_like(arr)
    cdef int n = arr.shape[0]

    vrda_cos(n, <double*>arr.data, <double*>out.data)
    return out

def exp(np.ndarray[np.float64_t] arr):
    cdef np.ndarray[np.float64_t] out = np.empty_like(arr)
    cdef int n = arr.shape[0]

    vrda_exp(n, <double*>arr.data, <double*>out.data)
    return out

def log(np.ndarray[np.float64_t] arr):
    cdef np.ndarray[np.float64_t] out = np.empty_like(arr)
    cdef int n = arr.shape[0]

    vrda_log(n, <double*>arr.data, <double*>out.data)
    return out

def log10(np.ndarray[np.float64_t] arr):
    cdef np.ndarray[np.float64_t] out = np.empty_like(arr)
    cdef int n = arr.shape[0]

    vrda_log10(n, <double*>arr.data, <double*>out.data)
    return out

def log2(np.ndarray[np.float64_t] arr):
    cdef np.ndarray[np.float64_t] out = np.empty_like(arr)
    cdef int n = arr.shape[0]

    vrda_log2(n, <double*>arr.data, <double*>out.data)
    return out

