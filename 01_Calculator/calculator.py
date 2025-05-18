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