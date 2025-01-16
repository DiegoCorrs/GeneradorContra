
import string
import random

#establece la longitud de la contraseña
longitud = int(input("ingrese el tamaño de la contraseña: "))

#genera los caracteres para usar en la contraseña
caracteres = string.ascii_letters + string.digits + string.punctuation

#genera aleatorimente la contraseña con la longitud especificada
contrasena = "".join(random.choice(caracteres) for i in range(longitud))

print("la contraseña generada es: ", contrasena)
