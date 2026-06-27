import pytest
from maths import calcular_cuadrado

def test_calcular_cuadrado():
    assert calcular_cuadrado(5) == 25
    assert calcular_cuadrado(0) == 0
    assert calcular_cuadrado(-3) == 9
    print("Las pruebas se ejecutaron correctamente")

test_calcular_cuadrado()