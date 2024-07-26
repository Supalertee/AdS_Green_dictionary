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








expected_matrix_Bxss = np.array(eval(open('test_Bxss.txt').read()))      

def test_matrix_Bx_ss():

    output_matrix = Gd.Bxss.G(1,1,1,1)
    assert output_matrix.shape == expected_matrix_Bxss.shape
    
    for i in range(expected_matrix_ss.shape[0]):
        for j in range(expected_matrix_ss.shape[1]):
            assert pytest.approx(output_matrix[i, j],abs=1e-2)  == pytest.approx(expected_matrix_Bxss[i, j], abs=1e-2)

def test_matrix_Bx_ss_trace():
    output_matrix = np.trace(Gd.Bxss.G(1,1,1,1))
    assert pytest.approx(np.trace(expected_matrix_Bxss),abs=1e-2)  == pytest.approx(output_matrix, abs=1e-2)


expected_matrix_Bxsa = np.array(eval(open('test_Bxsa.txt').read()))      

def test_matrix_Bx_sa():

    output_matrix = Gd.Bxsa.G(1,1,1,1)
    assert output_matrix.shape == expected_matrix_Bxsa.shape
    
    for i in range(expected_matrix_ss.shape[0]):
        for j in range(expected_matrix_ss.shape[1]):
            assert pytest.approx(output_matrix[i, j],abs=1e-2)  == pytest.approx(expected_matrix_Bxsa[i, j], abs=1e-2)

def test_matrix_Bx_sa_trace():
    output_matrix = np.trace(Gd.Bxsa.G(1,1,1,1))
    assert pytest.approx(np.trace(expected_matrix_Bxsa),abs=1e-2)  == pytest.approx(output_matrix, abs=1e-2)







expected_matrix_Bxyss = np.array(eval(open('test_Bxyss.txt').read()))      

def test_matrix_Bxy_ss():

    output_matrix = Gd.Bxyss.G(1,1,1,1)
    assert output_matrix.shape == expected_matrix_Bxyss.shape
    
    for i in range(expected_matrix_Bxyss.shape[0]):
        for j in range(expected_matrix_Bxyss.shape[1]):
            assert pytest.approx(output_matrix[i, j],abs=1e-2)  == pytest.approx(expected_matrix_Bxyss[i, j], abs=1e-2)

def test_matrix_Bxy_ss_trace():
    output_matrix = np.trace(Gd.Bxyss.G(1,1,1,1))
    assert pytest.approx(np.trace(expected_matrix_Bxyss),abs=1e-2)  == pytest.approx(output_matrix, abs=1e-2)


# expected_matrix_Bxysa = np.array(eval(open('test_Bxysa.txt').read()))      

# def test_matrix_Bxy_sa():

#     output_matrix = Gd.Bxyss.G(1,1,1,1)
#     assert output_matrix.shape == expected_matrix_Bxysa.shape
    
#     for i in range(expected_matrix_Bxysa.shape[0]):
#         for j in range(expected_matrix_Bxysa.shape[1]):
#             assert pytest.approx(output_matrix[i, j],abs=1e-2)  == pytest.approx(expected_matrix_Bxysa[i, j], abs=1e-2)

# def test_matrix_Bxy_sa_trace():
#     output_matrix = np.trace(Gd.Bxyss.G(1,1,1,1))
#     assert pytest.approx(np.trace(expected_matrix_Bxysa),abs=1e-2)  == pytest.approx(output_matrix, abs=1e-2)
