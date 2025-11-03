# number = int(input("Inserisci un numero: "))

# print(f"la radice quadrata di {number} è {number ** 0.5}")

def is_prime(n):
    try:
        for number in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    except n <= 1:
        return False

if __name__ == "__main__":
    n = int(input("Inserisci un numero: "))
    if is_prime(n):
        print(f"{n} è un numero primo.")
    else:
        print(f"{n} non è un numero primo.")