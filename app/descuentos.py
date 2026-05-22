def calcular_descuento(compras_cliente: int) -> float:
    """
    Calcula el descuento para un cliente según su número de compras.

    Ticket Jira: SI-104
    Estado actual con error:
    - Cliente con más de 5 compras debería recibir 10%
    - Actualmente está retornando 5%

    TODO del estudiante:
    Modificar esta función para que:
    - Si compras_cliente > 5 retorne 0.10
    - Si compras_cliente <= 5 retorne 0.05
    """
    if compras_cliente > 5:
        return 0.05  # ERROR INTENCIONAL: debe ser 0.10
    return 0.05
