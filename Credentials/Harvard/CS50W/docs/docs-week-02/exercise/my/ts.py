def neg_converter(n):
    #return n if n >= 0 else n * -1
    #return n if n >= 0 else -n
    return abs(n)

x = int(input("Inserisci un numero: "))
print(neg_converter(x))
print(type(neg_converter(x)))


