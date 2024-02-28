import getpass
import string

password = getpass.getpass("ingrese la password: ").lower()

count = 0

for letra in password:
    for letra2 in string.ascii_lowercase:
        if letra == letra2:
            count += 1
            break
        else:
            count += 1

print(f"La contraseña fue forzada en {count} intentos")

