import requests

HELP_STRING = """
Ange ett år och fält
Exempelvis: 1965 fysik

Till exempel: 1965 physics

Fält: fysik, kemi, litteratur, ekonomi, fred, medicin

Tryck H för hjälp. 
Tryck Q för att avsluta.
"""

CAT = {"fysik": "phy",
       "kemi": "che",
       "litteratur": "lit",
       "ekonomi": "eco",
       "fred": "pea",
       "medicin": "med"}


def get_nobel_prizes(year, category):
    """ hämtar nobelprisvinnare, från år och inom vilken katgori"""

    params = {"nobelPrizeYear": year, "nobelPrizeCategory": category}
    res = requests.get("http://api.nobelprize.org/2.1/nobelPrizes", params=params).json()
    return res["nobelPrizes"]


def print_winners(winners):
    """hämtar ut vinnare/vinnarna med fullnamn och prisinformation"""

    for i, winner in enumerate(winners):
        print("-" * 10)
        print(f"{winner['categoryFullName']['se']} Prize")
        print(f"Amount: {winner['prizeAmount']} SEK")
        print("Winners:")
        for j, laureate in enumerate(winner["laureates"]):
            print(laureate['knownName']['en'])
            print(f"Motivation: {laureate['motivation']['en']}")
            if j < len(winner["laureates"]) - 1:
                print("-" * 10)


def print_summary(year, category, year_sum, num_winners):
    """hämtar en summering av år, kategori, antal år, och antal vinnare"""

    print("=" * 10)
    print(f"Total prize amount for {category} in year {year}: {year_sum} SEK")
    print(f"Number of winners: {num_winners}")
