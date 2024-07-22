import numpy as np
import Green_dict as Gd
import pytest


expected_matrix = np.array(eval(open('test.txt').read()))

def test_matrix():
    output_matrix = Gd.Bxss.G(1,1,1,1)
    
    assert output_matrix.shape == expected_matrix.shape
    
    for i in range(expected_matrix.shape[0]):
        for j in range(expected_matrix.shape[1]):
            assert output_matrix[i, j]  == pytest.approx(expected_matrix[i, j], 
                                                          abs=1e-4)
            
