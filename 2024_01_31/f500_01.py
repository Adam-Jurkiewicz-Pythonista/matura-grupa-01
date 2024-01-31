import csv  # https://docs.python.org/3/library/csv.html

with open("f500.csv", "r", encoding="UTF-8") as f500:
    csvreader = csv.reader(f500)

    print(f"{csvreader=}")
    for i, element in enumerate(csvreader):
        print(f"{i=} || {element=}")