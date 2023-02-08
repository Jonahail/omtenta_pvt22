import Omtenta2


def main():
    help_shown = False

    while True:
        if not help_shown:
            print(Omtenta2.HELP_STRING)
            help_shown = True

        aaa = input(">")
        if aaa.lower() in ["q", "h"]:
            if aaa.lower() == "q":
                break
            else:
                continue

        aaa = aaa.split()
        if len(aaa) != 2:
            print("Incorrect input format, enter year and field.")
            continue

        try:
            year, category = int(aaa[0]), aaa[1].lower()
        except:
            print("Incorrect input format, enter a valid year and field.")
            continue

        if category not in Omtenta2.CAT:
            print("Invalid field, enter one of the available fields.")
            continue

        category = Omtenta2.CAT[category]
        prizes = Omtenta2.get_nobel_prizes(year, category)

        if not prizes:
            print(f"No prizes found for {category} in year {year}")
            continue

        year_sum = 0
        num_winners = 0
        for prize in prizes:
            year_sum += prize["prizeAmount"]
            num_winners += len(prize["laureates"])

        Omtenta2.print_winners(prizes)


if __name__ == '__main__':
    main()
