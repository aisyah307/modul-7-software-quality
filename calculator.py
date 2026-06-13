import os

def add(a: float, b: float) -> float:
    return a + b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Divider cannot be zero")
    return a / b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def power(a: float, b: float) -> float:
    return a ** b

def dummy_function():
    return "Fungsi ini sengaja tidak dites"

def check_number_status(x: float) -> str:
    if x > 100:
        if x % 2 == 0:
            return "Large Even"
        else:
            return "Large Odd"
    elif x < 0:
        return "Negative"
    else:
        return "Normal"
