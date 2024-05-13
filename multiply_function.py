def multiply(a, b):
    """
    Returns the result of multiplying two numbers.
    """
    return a * b

# Esta función fue corregida del error de multiplicar por cero
def multiply_by_zero(a):
    """
    Returns 0 when multiplying a number by zero.
    """
    if a == 0:
        return 0
    else:
        return a
