# ✅ Testovací případ (Test Case) - Funkce addition()
<!-- Ikony ✅ Pass / ❌ Fail -->

### **ID případu:** TC01  

**Název:** Sčítání dvou kladných celých čísel 

**Scénář:** [TS01](test_scenarios.md#id-scénáře-ts01)

**Kroky:**  
1. Otevři terminál a přejdi do složky, kde se nachází soubor `calculator.py`
2. Spusť aplikaci pomocí příkazu `python calculator.py`
3. Na výzvu **Zadej číslo operace:** zadej číslo `1`
4. Na výzvu "Zadej první číslo:" zadej `2` a potvrď klávesou **Enter**
5. Na výzvu "Zadej druhé číslo:" zadej `3` a potvrď klávesou **Enter**
6. Zkontroluj výstup v terminálu

**Vstupy:** 1. číslo: `2` a 2. číslo: `3` 

**Očekávaný výstup:** `Výsledek: 2.0 + 3.0 = 5.0`

**Skutečný výstup:** `Výsledek: 2.0 + 3.0 = 5.0`

**Printscreen výstupu:** [TC_01_output](screenshots/tc01_output.png)

**Výsledek:** ✅ Pass 

**Poznámky:** -

---

### **ID případu:** TC02

**Název:** Sčítání dvou celých čísel (Kladné / Záporné)

**Scénář:** [TS01](test_scenarios.md#id-scénáře-ts01)

**Kroky:**
1. Otevři terminál a přejdi do složky, kde se nachází soubor `calculator.py`
2. Spusť aplikaci pomocí příkazu `python calculator.py`
3. Na výzvu **Zadej číslo operace:** zadej číslo `1`
4. Na výzvu "Zadej první číslo:" zadej `2` a potvrď klávesou **Enter**
5. Na výzvu "Zadej druhé číslo:" zadej `-5` a potvrď klávesou **Enter**
6. Zkontroluj výstup v terminálu

**Vstupy:** 1. číslo: `2` a 2. číslo: `-5` 

**Očekávaný výsledek:** `Výsledek: 2.0 + -5.0 = -3.0`

**Skutečný výsledek:** `Výsledek: 2.0 + -5.0 = -3.0`

**Printscreen výstupu:** [TC_02_output](screenshots/tc02_output.png)

**Výsledek:** ✅ Pass

**Poznámky:** 
- [ ] Pokud je druhé číslo záporné, zvážil bych přidání dát číslo do závorek pro lepší UI 

---

### **ID případu:** TC03

**Název:** Sčítání dvou celých čísel (Záporné/Kladné)

**Scénář:** [TS01](test_scenarios.md#id-scénáře-ts01)

**Kroky:**
1. Otevři terminál a přejdi do složky, kde se nachází soubor `calculator.py`
2. Spusť aplikaci pomocí příkazu `python calculator.py`
3. Na výzvu **Zadej číslo operace:** zadej číslo `1`
4. Na výzvu **Zadej první číslo:** zadej číslo `-2` a potvrď klávesou **Enter**
5. Na výzvu "Zadej druhé číslo:" zadej `5` a potvrď klávesou **Enter**
6. Zkontroluj výstup v terminálu 

**Vstupy:** 1. číslo: `-2` a 2. číslo: `5` 

**Očekávaný výsledek:** `Výsledek: -2.0 + 5.0 = 3.0`

**Skutečný výsledek:** `Výsledek: -2.0 + 5.0 = 3.0`

**Printscreen výstupu:** [TC_03_output](screenshots/tc03_output.png)

**Výsledek:** ✅ Pass

**Poznámky** -

--- 

### **ID případu:** TC04

**Název:** Sčítání dvou celých čísel (Záporné/Záporné)

**Scénář:** [TS01](test_scenarios.md#id-scénáře-ts01)

**Kroky:**
1. Otevři terminál a přejdi do složky, kde se nachází soubor `calculator.py`
2. Spusť aplikaci pomocí příkazu `python calculator.py`
3. Na výzvu **Zadej číslo operace:** zadej číslo `1`
4. Na výzvu **Zadej první číslo:** zadej číslo `-2` a potvrď klávesou **Enter**
5. Na výzvu "Zadej druhé číslo:" zadej `-5` a potvrď klávesou **Enter**
6. Zkontroluj výstup v terminálu 

**Vstupy:** 1. číslo: `-2` a 2. číslo: `-5` 

**Očekávaný výsledek:** `Výsledek: -2.0 + -5.0 = -7.0`

**Skutečný výsledek:** Netestováno

**Printscreen výstupu:** - 

**Výsledek:** - 

**Poznámky** -

---

### **ID případu:** TC05

**Název:** Sčítání dvou desetinných kladných čísel (Kladné / Kladné)

**Scénář:** [TS01](test_scenarios.md#id-scénáře-ts01)

**Kroky:**
1. Otevři terminál a přejdi do složky, kde se nachází soubor `calculator.py`
2. Spusť aplikaci pomocí příkazu `python calculator.py`
3. Na výzvu **Zadej číslo operace:** zadej číslo `1`
4. Na výzvu **Zadej první číslo:** zadej číslo `2.3` a potvrď klávesou **Enter**
5. Na výzvu "Zadej druhé číslo:" zadej `5.2` a potvrď klávesou **Enter**
6. Zkontroluj výstup v terminálu 

**Vstupy:** 1. číslo: `2.3` a 2. číslo: `5.2` 

**Očekávaný výsledek:** `Výsledek: 2.3 + 5.2 = 7.5`

**Printscreen výstupu:** -

**Skutečný výsledek:** Netestováno

**Výsledek:** - 

**Poznámky** -

---

### **ID případu:** TC06

**Název:** Sčítání dvou desetinných čísel (Kladné / Záporné)

**Scénář:** [TS01](test_scenarios.md#id-scénáře-ts01)

**Kroky:**
1. Otevři terminál a přejdi do složky, kde se nachází soubor `calculator.py`
2. Spusť aplikaci pomocí příkazu `python calculator.py`
3. Na výzvu **Zadej číslo operace:** zadej číslo `1`
4. Na výzvu **Zadej první číslo:** zadej číslo `2.3` a potvrď klávesou **Enter**
5. Na výzvu "Zadej druhé číslo:" zadej `-5.2` a potvrď klávesou **Enter**
6. Zkontroluj výstup v terminálu 

**Vstupy:** 1. číslo: `2.3` a 2. číslo: `-5.2` 

**Očekávaný výsledek:** `Výsledek: 2.3 + -5.2 = -2.9`

**Skutečný výsledek:** Netestováno

**Printscreen výstupu:** -

**Výsledek:** - 

**Poznámky** -

--- 

### **ID případu:** TC07

**Název:** Sčítání dvou desetinných čísel (Záporné / Kladné)

**Scénář:** [TS01](test_scenarios.md#id-scénáře-ts01)

**Kroky:**
1. Otevři terminál a přejdi do složky, kde se nachází soubor `calculator.py`
2. Spusť aplikaci pomocí příkazu `python calculator.py`
3. Na výzvu **Zadej číslo operace:** zadej číslo `1`
4. Na výzvu **Zadej první číslo:** zadej číslo `-2.3` a potvrď klávesou **Enter**
5. Na výzvu "Zadej druhé číslo:" zadej `5.2` a potvrď klávesou **Enter**
6. Zkontroluj výstup v terminálu 

**Vstupy:** 1. číslo: `-2.3` a 2. číslo: `5.2` 

**Očekávaný výsledek:** `Výsledek: -2.3 + 5.2 = 2.9`

**Skutečný výsledek:** Netestováno

**Printscreen výstupu:** -

**Výsledek:** - 

**Poznámky** -

---

### **ID případu:** TC08

**Název:** Sčítání dvou desetinných čísel (Záporné / Záporné)

**Scénář:** [TS01](test_scenarios.md#id-scénáře-ts01)

**Kroky:**
1. Otevři terminál a přejdi do složky, kde se nachází soubor `calculator.py`
2. Spusť aplikaci pomocí příkazu `python calculator.py`
3. Na výzvu **Zadej číslo operace:** zadej číslo `1`
4. Na výzvu **Zadej první číslo:** zadej číslo `-2.3` a potvrď klávesou **Enter**
5. Na výzvu "Zadej druhé číslo:" zadej `-5.2` a potvrď klávesou **Enter**
6. Zkontroluj výstup v terminálu 

**Vstupy:** 1. číslo: `-2.3` a 2. číslo: `-5.2` 

**Očekávaný výsledek:** `Výsledek: -2.3 + -5.2 = -7.5`

**Skutečný výsledek:** Netestováno

**Printscreen výstupu:** -

**Výsledek:** - 

**Poznámky** -

---

### **ID případu:** TC09

**Název:** Sčítání jeden prázdný vstup jedno celé číslo ( null / Kladné)

**Scénář:** [TS01](test_scenarios.md#id-scénáře-ts01)

**Kroky:**
1. Otevři terminál a přejdi do složky, kde se nachází soubor `calculator.py`
2. Spusť aplikaci pomocí příkazu `python calculator.py`
3. Na výzvu **Zadej číslo operace:** zadej číslo `1`
4. Na výzvu **Zadej první číslo:** potvrď klávesou **Enter**
5. Na výzvu "Zadej druhé číslo:" zadej `-5.2` a potvrď klávesou **Enter**
6. Zkontroluj výstup v terminálu 

**Vstupy:** 1. číslo: a 2. číslo: `-5.2` 

**Očekávaný výsledek:** `Nelze spočítat nezadal si 1. číslo`

**Skutečný výsledek:** Netestováno

**Printscreen výstupu:** -

**Výsledek:** - 

**Poznámky** -
