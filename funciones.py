def primo(num):
    for i in range(2, (num**0.5)+1):
        if num % i == 0:
            print("El numero", num, "no es primo")
        else:
            print("El numero", num, "es primo")