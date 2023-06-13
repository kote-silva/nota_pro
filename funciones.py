def primo(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            print("El numero", num, "no es primo")
            return

    x = print("El numero", num, "es primo")



def primos(num):
    primos=[]
    for i in range(0, num+1):
        if primo(i):
            primos.append(i)
    print(primos)
    return primos

            
a = int(input("Agrega el numero que deseas comprobar --> "))
primo(a)
primos(a)