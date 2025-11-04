import sys
import math

class Prime:
    def __init__(self, n):
        self.n = n

    def input_check(self):
        try:
            return int(self.n)
        except (ValueError, TypeError):
            print("Error: Invalid input.")
            sys.exit(1)

    def is_prime(self):
        n = self.input_check()
        if n <= 1:
            return False
        # limit = int(n**0.5)
        limit = math.isqrt(n)
        for d in range(2, limit + 1):
            if n % d == 0:
                return False
        return True

if __name__ == "__main__":
    user_input = input("Enter a number: ")
    prime_checker = Prime(user_input)
    print("Prime" if prime_checker.is_prime() else "Not prime")


# we can easely optimize the is_prime using the 6k +/- 1 rule
# but this is sufficient for small numbers