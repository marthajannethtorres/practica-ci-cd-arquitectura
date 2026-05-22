from descuentos import calcular_descuento

def test_descuento_cliente_normal():
    assert calcular_descuento(3) == 0.05

def test_descuento_cliente_frecuente():
    assert calcular_descuento(6) == 0.10
