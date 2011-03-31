
import numpy as np
cimport numpy as np

# ACML vector  functions 
cdef extern from "acml_mv.h":
    int vrda_sin(int n, double a[], double y[])
    int vrda_cos(int n, double a[], double y[])
    int vrda_exp(int n, double a[], double y[])
    int vrda_log(int n, double a[], double y[])
    int vrda_log2(int n, double a[], double y[])
    int vrda_log10(int n, double a[], double y[])


##############################################################################
# Function wrappers
    
def sin(int n, np.ndarray[np.float64_t] arr, np.ndarray[np.float64_t] out):
    vrda_sin(n, <double*>arr.data, <double*>out.data)

def cos(int n, np.ndarray[np.float64_t] arr, np.ndarray[np.float64_t] out):
    vrda_cos(n, <double*>arr.data, <double*>out.data)

def exp(int n, np.ndarray[np.float64_t] arr, np.ndarray[np.float64_t] out):
    vrda_exp(n, <double*>arr.data, <double*>out.data)

def log(int n, np.ndarray[np.float64_t] arr, np.ndarray[np.float64_t] out):
    vrda_log(n, <double*>arr.data, <double*>out.data)

def log2(int n, np.ndarray[np.float64_t] arr, np.ndarray[np.float64_t] out):
    vrda_log2(n, <double*>arr.data, <double*>out.data)

def log10(int n, np.ndarray[np.float64_t] arr, np.ndarray[np.float64_t] out):
    vrda_log10(n, <double*>arr.data, <double*>out.data)

