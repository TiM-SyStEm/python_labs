import csv
import json

from src.lab05.csv_xlsx import csv_to_xlsx


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Read JSON-file and convert to CSV-file.

    Input data
    ----------
    json_path: str
    csv_path: str

    Returns
    -------
    None

    Raises
    ------
    ValueError: JSON-file is empty or invalid structure.
    ValueError: JSON isn't list of dicts.
    """
    with open(json_path, "r", encoding="utf-8") as f:
        try:
            data: list [dict] = json.load(f)
        except json.decoder.JSONDecodeError:
            raise ValueError("JSON-file is empty or invalid structure.")

        header = data[0].keys()

        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            try:
                w = csv.DictWriter(f, fieldnames=header)
                w.writeheader()
                w.writerows(data)
            except ValueError:
                raise ValueError("JSON-file is empty or invalid structure.")
            except AttributeError:
                raise ValueError("JSON isn't list of dicts.")

def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Read CSV-file and convert to JSON-file.

    Input data
    ----------
    csv_path: str
    json_path: str

    Returns
    -------
    None

    Raises
    ------
    ValueError: CSV-file is empty or invalid structure.
    """

    with open(csv_path, "r", encoding="utf-8") as f:
        # Get information about CSV-file
        sample = f.read(1024)
        try:
            dialect = csv.Sniffer().sniff(sample)
        except csv.Error:
            raise ValueError("CSV-file is empty or invalid structure.")

        f.seek(0)
        reader = csv.DictReader(f, dialect=dialect)

        data = list(reader)

        if reader.fieldnames == []:
            raise ValueError("CSV-file is empty or invalid structure.")

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
