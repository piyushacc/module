import pytest
from main import classify_triangle, calculate_discounted_price

@pytest.mark.parametrize("a,b,c,expected", [
    (3, 3, 3, "Equilateral"),
    (3, 4, 4, "Isosceles"),
    (3, 4, 5, "Scalene"),
    (1, 2, 3, "Not a triangle"),  
    (0, 4, 5, "Not a triangle"),  
    (-1, 4, 5, "Not a triangle"), 
])
def test_classify_triangle(a, b, c, expected):
    assert classify_triangle(a, b, c) == expected

@pytest.mark.parametrize("price,discount,expected", [
    (100, 0, 100.00),
    (100, 50, 50.00),
    (100, 100, 0.00),
    (99.99, 25, 74.99),
])
def test_calculate_discounted_price(price, discount, expected):
    assert calculate_discounted_price(price, discount) == expected

