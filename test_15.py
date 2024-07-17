def calculate_rectangle_perimeter(l, w):
    if l <= 0 or w <= 0:
        raise ValueError("Length and width must be positive numbers!")
    return 2 * (l + w)


print(calculate_rectangle_perimeter(-5, 10))

#AI understands the context