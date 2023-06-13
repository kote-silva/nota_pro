def primo(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            print("El numero", num, "no es primo")
            return

    print("El numero", num, "es primo")


a = int(input("Agrega el numero que deseas comprobar --> "))
primo(a)