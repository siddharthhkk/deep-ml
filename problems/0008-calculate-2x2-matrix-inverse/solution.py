def inverse_2x2(m: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    # Your code here
    a, b = m[0][0], m[0][1]
    c, d = m[1][0], m[1][1]
    det = (a * d) - (b * c)
    if det == 0: return None
    return [
        [d/det, -b/det],
        [-c/det, -a/det]
    ]
    pass