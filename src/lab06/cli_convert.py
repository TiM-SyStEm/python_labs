import argparse

from src.lab05.csv_xlsx import csv_to_xlsx
from src.lab05.json_csv import csv_to_json, json_to_csv


def main():
    parser = argparse.ArgumentParser(description="Collection of data converters.")
    sub = parser.add_subparsers(dest="command")

    p1 = sub.add_parser("json2csv", help="Convert JSON-file to CSV-file.")
    p1.add_argument("--in", dest="input", required=True, help="")
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json", help="Convert CSV-file to JSON-file.")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx", help="Convert CSV-file to XLSX-file.")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    if args.command == "json2csv":
        json_to_csv(args.input, args.output)

    elif args.command == "csv2json":
        csv_to_json(args.input, args.output)

    elif args.command == "csv2xlsx":
        csv_to_xlsx(args.input, args.output)

if __name__ == "__main__":
    main()
