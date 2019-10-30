#!/usr/bin/env python
import numpy as np
import numpy.random
import pandas as pd
import fire
import time

# file load function
def read_from_csv(faile_path):
    matrixCSV = pd.read_csv(faile_path, header=None, index_col=False, delimiter = ',')

    numpy_matrix = matrixCSV.values

    a,b = numpy_matrix.shape
    return a, b, numpy_matrix

# adding additional fields (index does not go the bounds of the array)
def matrix_add_null(a, b, arr):
    arr =np.insert(arr, [0], [0], axis=1)
    arr =np.insert(arr, b+1, [0], axis=1)
    arr =np.insert(arr, [0], [[0]], axis=0)
    arr =np.insert(arr, a+1, [[0]], axis=0)
    return arr

# array processing function
def life(arr, a, b):
    print(arr[1:-1,1:-1],'\n')
    while np.sum(arr) != 0:
        time.sleep(1)
        check_matrix = [] 
        arr_etal = arr.copy()
        for i in range(1, a+1):
            for j in range(1, b+1):

                check_matrix = arr_etal[i-1:i+2, j-1:j+2]
                if arr_etal[i,j] == 1:
                    check = np.sum(check_matrix)-1
                else:
                    check = np.sum(check_matrix)
      
                if ((check < 2) or (check > 3)) and arr[i,j] == 1:
                    arr[i,j] = 0
                elif ((check == 2) or (check == 3)) and arr[i,j] == 1:
                    arr[i,j] = 1
                elif check == 3 and arr[i,j] == 0:
                    arr[i,j] = 1
                elif check != 3 and arr[i,j] == 0:
                    arr[i,j] = 0
        print(arr_etal[1:-1,1:-1],'\n')
        print(arr[1:-1,1:-1],'\n')

# load matrix from file
def from_file(faile_path='test.csv'):

    a,b,arr = read_from_csv(faile_path)
    arr = matrix_add_null(a,b,arr)

    life(arr, a, b)

# set the matrix with user parameters
def set_matrix(a,b):
    arr = []
    arr = np.random.randint(0, 2, (a, b))
    arr = matrix_add_null(a,b,arr)
    life(arr, a, b)


if __name__ == '__main__':
    fire.Fire({
        'from_file':from_file,
        'set_matrix':set_matrix
    })
