import ctypes

lib = ctypes.CDLL('my_calculator.so')

def add_numbers(a, b):
    lib.add_numbers.argtypes = [ctypes.c_int, ctypes.c_int]
    lib.add_numbers.restype = ctypes.c_int
    return lib.add_numbers(a, b)
