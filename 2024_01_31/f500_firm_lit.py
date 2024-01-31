import csv  # https://docs.python.org/3/library/csv.html

companies = {}
max_len_name = 0

with open("f500.csv", "r", encoding="UTF-8") as f500:
    csvreader = csv.reader(f500)

    print(f"{csvreader=}")
    for i, element in enumerate(csvreader):
        if i > 0:
            letter = element[0][0].upper()
            if letter not in companies:
                companies[letter] = 1
            else:
                companies[letter] += 1

            # wyszukanie największej ilości słów w nazwie
            len_name = len(element[0].split())
            if len_name > max_len_name:
                max_len_name = len_name
                max_name = element[0]

    print(f"{max_len_name=} | {max_name=}")

        # print(f"{i=} || {element=}")

    # print(f"{companies['A']=} {companies['D']=} {companies['E']=}")
    print(f"{companies=}")

    # sposób okrężny
    max_comp = max(companies.values())
    comps = list(companies.values())
    max_pos = comps.index(max_comp)
    max_lett = list(companies.keys())
    max_letter = max_lett[max_pos]
    print(f"{max_pos}")
    print(f"{comps=} | {max_comp=}")
    print(f"{max_lett=}")
    print(f"{max_letter=}")

    # sposób wprost idealny na maturę - wyszukiwanie max elem. w zbiorze
    max_companies = 0
    for element in companies:
        number = companies[element]
        if number > max_companies:
            max_companies = number
            letter_of_max_companies = element
    print(f"{letter_of_max_companies=} | {max_companies=}")


