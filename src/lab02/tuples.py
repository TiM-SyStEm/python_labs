def format_record(rec: tuple[str, str, float]) -> str:
    """
    It is format record (fio, griup, gpa) to string by rules.

    Inpurt data
    -----------
    rec: tuple[str, str, float]

    Returns
    -------
    Formated string from tuple.
        Type: str.
        Format examples: "Сидорова А.С., гр. ABB-01, GPA 4.00", "Петров П.;
                        гр. IKBO-12, GPA 5.00".

    Raises
    ------
    ValueError: Incorrect fio.
        When fio is empty.
    ValueError: Incorrect group.
        When group is empty.
    TypeError: Incorrect type for GPA.
        When type of GPA isn't float.
    """

    fio, group, gpa = rec
    while "  " in fio: fio = fio.replace("  ", " ")
    fio = fio.strip()

    if fio == "": raise ValueError("Incorrect fio.")
    if group == "": raise ValueError("Incorrect group.")
    if type(gpa) != float: raise TypeError("Incorrect type for GPA.")

    fio_spl = fio.split()
    inicialy = f"{fio_spl[0][0].upper()}{fio_spl[0][1::]} {fio_spl[1][0].upper()}. {fio_spl[2][0].upper()}."\
        if len(fio_spl) == 3 \
        else f"{fio_spl[0][0].upper()}{fio_spl[0][1::]} {fio_spl[1][0].upper()}."
    return f"{inicialy}, гр. {group}, GPA {gpa:.2f}"
