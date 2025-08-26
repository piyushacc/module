def classify_triangle(a: float, b: float, c: float) -> str:
    """
    Classifies a triangle based on side lengths a, b, c.
    Returns:
        - 'Equilateral' if all sides equal
        - 'Isosceles' if exactly two sides equal
        - 'Scalene' if all sides different
        - 'Not a triangle' if sides do not form a valid triangle
    """
    sides = sorted([a, b, c])
    if any(side <= 0 for side in sides):
        return 'Not a triangle'
    if sides[0] + sides[1] <= sides[2]:
        return 'Not a triangle'
    if a == b == c:
        return 'Equilateral'
    if a == b or b == c or a == c:
        return 'Isosceles'
    return 'Scalene'


def calculate_discounted_price(price: float, discount: float) -> float:
    """
    Calculates discounted price given original price and discount percentage.
    Handles edge cases where price < 0, discount < 0 or > 100.
    Returns:
        - discounted price rounded to 2 decimals
        - raises ValueError if inputs are invalid
    """
    if price < 0:
        raise ValueError("Price cannot be negative")
    if not (0 <= discount <= 100):
        raise ValueError("Discount must be between 0 and 100")
    discounted_price = price * (1 - discount / 100)
    return round(discounted_price, 2)
