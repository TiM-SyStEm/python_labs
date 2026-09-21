def transpose(mat: list[list[float | int]]) ->  list:
    """
    This function transposes rectangly matrice.

    Input data
    ----------
    mat: list [ list [float | int] ]
        Matrice.
    Returns
    -------
    Transposed matrice.
        Type: list[list]

    Raises
    ------
    ValueError: Matrice isn't rectangly.
    """

    if len(mat) == 0:
        return []
    else:
        m = len(mat)
        n = len(mat[0])
        new_mat: list[list[float | int]] = [[0 for _ in range(m)] for _ in range(n)]
        first_row = len(mat[0])
        for i in range(m):
            if len(mat[i]) != first_row:
                raise ValueError("Input matrice isn't rectangle matrice.")
            for j in range(n):
                new_mat[j][i] = mat[i][j]
        return new_mat


def row_sums(mat: list[list[float | int]]) -> list[float]:
    """
    This function takes matrice and returns list of sums by rows.

    Input data
    ----------
    mat: list[ list [float | int] ]
        Matrice.

    Returns
    -------
    List of sums by rows.
        Type: list[float]

    Raises
    ------
    ValueError: Input matrice isn't rectangle matrice.
    """

    # Check input matrice if it's rectangly.
    for r in mat:
        if len(r) != len(mat[0]):
            raise ValueError("Input matrice isn't rectangle matrice.")

    return [sum(mat[i]) for i in range(len(mat)) if len(mat[i]) == len(mat[0])]

def col_sums(mat: list[list[float | int]]) -> list[float]:
    """
    This function takes matrice and returns list of sums by collums.

    Input data
    ----------
    mat: list[ list [float | int] ]
        Matrice.

    Returns
    -------
    List of sums by collums.
        Type: list[float]

    Raises
    ------
    ValueError: Input matrice isn't rectangle matrice.
    """

    return row_sums(transpose(mat))
