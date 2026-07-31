def sum_all(*args: float | int) -> float | int:
    """
    Returns the sum of all provided numbers.
    """
    # Checking for non-numeric types to raise a clear error
    if not all(isinstance(x, (int, float)) for x in args):
        raise TypeError("All arguments must be integers or floats! understood?")
        
    return sum(args)