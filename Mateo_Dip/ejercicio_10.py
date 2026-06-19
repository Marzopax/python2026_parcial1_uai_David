from programa import calcular_cuadrado

def test_calcular_cuadrado():
    
    assert calcular_cuadrado(4) == 16
    assert calcular_cuadrado(0) == 0