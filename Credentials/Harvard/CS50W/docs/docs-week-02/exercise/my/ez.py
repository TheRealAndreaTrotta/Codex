'''
# Facile — Analizzatore di numero

**Obiettivo**
• Chiedi un numero intero all’utente e stampa:

* se è **positivo/negativo/zero**
* se è **pari/dispari**

**Criteri di successo**
• Input: `-3` → Output: `negativo, dispari`
• Input: `0` → Output: `zero, pari`
• Gestisci input non valido con un messaggio d’errore pulito (niente stacktrace).
'''
import sys

class NumberType():
    def __init__(self, n):
        try:
            self.n = int(n)
        except ValueError:
            print("Error: Invalid input.")
            sys.exit(1)

    def positive_negative_zero(self):
        if self.n > 0:
            return "positive"
        elif self.n < 0:
            return "negative"
        else:
            return "zero"

    def even_or_odd(self):
        return "even" if self.n % 2 == 0 else "odd"
    
    def check(self):
        return self.positive_negative_zero(), self.even_or_odd()




if __name__ == "__main__":
    n = input("Enter an integer: ")
    analyzer = NumberType(n)
    kind, parity = analyzer.check()
    print(f"{kind}, {parity}")


def international_float_parser(s):
    #Parse a float from a string, handling both commas and dots as decimal separators.
    s = s.replace(',', '.')
    try:
        return float(s)
    except ValueError:
        print("Error: Invalid float format.")
        sys.exit(1)