"""
convenience methods to parse css transforms 
"""
import numpy as np

def parse_css_transform_matrix(m:str)->np.array:
    """
    Parse matrix of css transform property
    e.g., m = element.value_of_css_property("transform")
    where m = 'matrix(6.12323e-17, -1, 1, 6.12323e-17, 0, 0)'
    return matrix as a np.array of float values with shape (6,1)
    """
    a = m.split('(')[1].split(')')[0]
    c = a.split(',')
    m = [np.float(i) for i in c]
    matrix = np.array(m)
    return matrix

def css_matrix_rotation(matrix:np.array)->float:
    """
    input is np.array with shape (6,1)
    e.g.. matrix = [6.12323e-17, -1, 1, 6.12323e-17, 0, 0)]
    return: float angle in degrees
    """
    assert np.shape(matrix) == (6,)
    alpha = matrix[0]
    beta = matrix[1]
    scale = np.sqrt(np.power(alpha,2) + np.power(beta,2))
    sin = beta/scale
    angle = np.round(np.arcsin(sin) * (180 / np.pi))
    return angle

def css_matrix_translation(matrix:np.array)->tuple:
    """
    input is np.array with shape (6,1)
    e.g.. matrix = [6.12323e-17, -1, 1, 6.12323e-17, 0, 0)]
    return: ordered tuple of float values for x and y translation
    """      
    assert np.shape(matrix) == (6,)
    x = matrix[4]
    y = matrix[5]          
    return (x,y)
