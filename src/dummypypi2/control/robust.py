"""This is a dummy implementation of various robust control algorithms"""

import numpy as np


def frob_norm(matrix):
    """Compute the Frobenius norm of a matrix"""
    return np.linalg.norm(matrix, 'fro')