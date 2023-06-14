def primo(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return True
    return False


def primos(num):
    primos=[]
    for i in range(2, num+1):
        if primo(i) == False:
            primos.append(i)
    print(primos)
    return primos

            
a = int(input("Agrega el numero que deseas comprobar --> "))
if primo(a) == False:
    print("El numero", a, "es primo")
else:
    print("El numero", a, "no es primo")
    
d = input("¿Deseas ver los numero primos anteriores?")
if d == "si" or d == "Si":
    primos(a)