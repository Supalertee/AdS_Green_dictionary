import numpy as np
import Green_dict as Gd
import pytest
import os

os.chdir(os.path.join(str(os.getcwd()), "unit_testing"))

expected_matrix_ss = np.array(eval(open('test_scalarss.txt').read()))

def test_matrix_scalar_ss():
    output_matrix = Gd.Scalarss.G(1,1,1,1)
    assert output_matrix.shape == expected_matrix_ss.shape
    
    for i in range(expected_matrix_ss.shape[0]):
        for j in range(expected_matrix_ss.shape[1]):
            assert pytest.approx(output_matrix[i, j],abs=1e-2)  == pytest.approx(expected_matrix_ss[i, j], abs=1e-2)


def test_matrix_scalar_ss_trace():
    output_matrix = np.trace(Gd.Scalarss.G(1,1,1,1))
    assert pytest.approx(np.trace(expected_matrix_ss),abs=1e-2)  == pytest.approx(output_matrix, abs=1e-2)



expected_matrix_sa = np.array(eval(open('test_scalarsa.txt').read()))

def test_matrix_scalar_sa():
    output_matrix = Gd.Scalarsa.G(1,1,1,1)
    
    assert output_matrix.shape == expected_matrix_sa.shape
    
    for i in range(expected_matrix_sa.shape[0]):
        for j in range(expected_matrix_sa.shape[1]):
            assert pytest.approx(output_matrix[i, j],abs=1e-2)  == pytest.approx(expected_matrix_sa[i, j], abs=1e-2)
            
def test_matrix_scalar_sa_trace():
    output_matrix = np.trace(Gd.Scalarsa.G(1,1,1,1))
    assert pytest.approx(np.trace(expected_matrix_sa),abs=1e-2)  == pytest.approx(output_matrix, abs=1e-2)



expected_matrix_Bss = np.array(eval(open('test_Bxss.txt').read()))      

def test_matrix_Bx_ss():

    output_matrix = Gd.Bxss.G(1,1,1,1)
    assert output_matrix.shape == expected_matrix_Bss.shape
    
    for i in range(expected_matrix_ss.shape[0]):
        for j in range(expected_matrix_ss.shape[1]):
            assert pytest.approx(output_matrix[i, j],abs=1e-2)  == pytest.approx(expected_matrix_Bss[i, j], abs=1e-2)

1