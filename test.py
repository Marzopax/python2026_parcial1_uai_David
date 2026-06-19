from ejercicio_10 import calcular_cuadrado

def test_calcular_cuadrado():
    assert calcular_cuadrado(5) == 25
    assert calcular_cuadrado(0) == 0
    assert calcular_cuadrado(-3) == 9