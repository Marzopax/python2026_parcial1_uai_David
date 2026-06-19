def calcular_cuadrado(n):
    return n * n


def test_calcular_cuadrado():
    assert calcular_cuadrado(4) == 16
    
    assert calcular_cuadrado(0) == 0