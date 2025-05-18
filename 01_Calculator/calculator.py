# První projekt Kalkulačka

# Funkce addition - sčítání dvou čísel
def addition(number1: float, number2: float) -> float:
    """
    Funkce sečte dvě desetinná čísla a vrátí jejich součet

    Args:
        number1 (float): První číselný vstup
        number2 (float): Druhý číselný vstup

    Returns:
        float: Výsledek součtu number1 a number2 
    """
    return number1 + number2

# Funkce subtraction . odčítání dvou čísel
def subtraction(number1: float, number2: float) -> float:
    """
    Funkce odečte dvě desetinná čísla a vrátí jejich rozdíl

    Args:
        number1 (float): První číselný vstup
        number2 (float): Druhý číselný vstup
    
    Returns:
        float: Výsledek rozdílu number1 a number2
    """
    return number1 - number2

# Funkce multiplication - násobení dvou čísel 
def multiplication(number1: float, number2: float) -> float:
    """
    Funkce vynásobí dvě desetinná čísla a vrátí jejich součin

    Args: 
        number1 (float): První číselný vstup
        number2 (float): Druhý číselný vstup

    Returns:
        float: Výsledek součinu number1 a number2
    """
    return number1 * number2

# Funkce divide - dělení dvou čísel
def divide(number1: float, number2: float) -> float:
    """
    Funkce vydělí dvě desetinná čísla a  vrítá jejich podíl. Zároveň je ošetřena chyba, že 0 nelze dělit

    Args:
        number1 (float): První číselný vstup
        number2 (float): Druhý číselný vstup

    Returns:
        float: Výsledek podílu number1 a number2
    """
    if number2 == 0:
        raise ZeroDivisionError("Nulou nelze dělit")
    return number1 / number2

def main_menu():
    print("Ahoj vítej v Kalkulačce níže si můžeš vybrat matematickou operaci a já ti to vypočítám")
    print("Matematické operace: ")
    print("1. Sčítání ")
    print("2. Odčítání ")
    print("3. Násobení ")
    print("4. Dělení ")
    volba = int(input("Zadej číslo operace: "))
    number1 = float(input("Zadej první číslo: "))
    number2 = float(input("Zadej druhé číslo: "))
    operace = ""

    if volba == 1: 
        operace = "Sčítání"
        print(f"Super, vybíráš si volbu: {volba} : {operace}")
        vysledek = addition(number1, number2)
        print(f"Výsledek: {number1} + {number2} = {vysledek}")

if __name__ == "__main__":
    main_menu()