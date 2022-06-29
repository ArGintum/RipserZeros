from __future__ import print_function
import ctypes
import sys
from .Ripser_plusplus_Converter import Ripser_plusplus_Converter, printHelpAndExit
from .Ripser_plusplus_Converter import find
import numpy as np
import scipy.sparse as sps
import os
import pathlib


'''
Runs ripser++ through user arguments.
args -- user arguments, given through CLI
data -- either a file name or a numpy array
'''
def run(args, data = None):
    
    # Split args
    params = args.split(' ')
    if "--help" in params:
        printHelpAndExit("Printing help")
    file_format = "distance"
    file_name = ""
    computational_mode = ""
    #print("\n------------RIPSER++ WITH PYTHON BINDINGS CALLED------------", sys.stderr)
    #print(params)
    i = 0
    while i < len(params):
        if params[i] == "--format":
            params[i] = ctypes.c_char_p(params[i].encode('utf-8'))
            if i+1 >= len(params):
                printHelpAndExit("Ripser++Python Error: No Format Specified")           
            else:
                file_format = params[i+1]#don't cast this, we need it as a Python type
                params[i+1]= ctypes.c_char_p(params[i+1].encode('utf-8'))
                i += 2
                continue
        elif params[i]=="--sparse":
            params[i] = ctypes.c_char_p(params[i].encode('utf-8'))
            i += 1
            continue
        elif params[i]=="--dim":
            params[i] = ctypes.c_char_p(params[i].encode('utf-8'))
            if i+1 >= len(params):
                printHelpAndExit("Ripser++Python Error: Dim not Specified")
            else:
                params[i+1] = ctypes.c_char_p(params[i+1].encode('utf-8'))
                i += 2
                continue
        elif params[i]=="--mode":
            params[i] = ctypes.c_char_p(params[i].encode('utf-8'))
            if i+1 >= len(params):
                printHelpAndExit("Ripser++Python Error: Mode not Specified")
            else:
                params[i+1] = ctypes.c_char_p(params[i+1].encode('utf-8'))
                computational_mode = params[i+1]
                i += 2
                continue
        elif params[i]=="--threshold":
            params[i] = ctypes.c_char_p(params[i].encode('utf-8'))
            if i+1 >= len(params):
                printHelpAndExit("Ripser++Python Error: Threshold not Specified")
            else:
                params[i+1] = ctypes.c_char_p(params[i+1].encode('utf-8'))
                i += 2
                continue
        elif params[i]=="--ratio":
            params[i] = ctypes.c_char_p(params[i].encode('utf-8'))
            if i+1 >= len(params):
                printHelpAndExit("Ripser++Python Error: Ratio not Specified")
            else:
                params[i+1] = ctypes.c_char_p(params[i+1].encode('utf-8'))
                i += 2
                continue
        elif i==(len(params)-1):
            params[i] = ctypes.c_char_p(params[i].encode('utf-8'))
            i += 1
            continue
        else:
            printHelpAndExit("Invalid Ripser++ Option") 
    
    matrix = []
    if data is not None and isinstance(data, str):
        file_name= ctypes.c_char_p(data.encode('utf-8'))
        matrix = None   
    elif data is not None and isinstance(data, np.ndarray):
        matrix = data
    elif data is not None and isinstance(data,sps.coo_matrix):
        matrix = data
    else:
        printHelpAndExit("Ripser++Python Error: Second argument must either be a string for file name, or a numpy array for input data")


    arguments = (ctypes.c_char_p * len(params)) ()
    arguments[:] = params
    
    prog = None
    path2= str(pathlib.Path(__file__).with_name('pyripser++.dll'))
    if None!=path2:
        prog2= ctypes.cdll.LoadLibrary(path2)
    else:
        raise Exception("Could not locate pyripser++.dll file, please check README.md for details.")

    path= str(pathlib.Path(__file__).with_name('pyripser++.dll'))
    if None != path:
          prog = ctypes.cdll.LoadLibrary(path)
    else:
        raise Exception("Could not locate pyripser++.dll file, please check README.md for details.")

    # Running python binding
    barcodes_dict = Ripser_plusplus_Converter(prog, arguments, file_name, file_format, computational_mode, matrix)
    return barcodes_dict
