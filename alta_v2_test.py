import requests, random, string

ip = 'localhost'

url = 'http://'+ip+'/Ejercicios/DWES/Repaso/ejerciciosServidor/3_Minijuegos_Juanma/app/php/index.php?accion=alta'

letras = string.ascii_letters + string.digits + '!@#$%^&*()'

while True:
    nombre = ''.join(random.choice(letras) for i in range(50))
    icono = ''.join(random.choice(letras) for i in range(100))
    enlace = ''.join(random.choice(letras) for i in range(255))
    requests.post(url, allow_redirects=False, data={
        'nombre': nombre,
        'icono': icono,
        'ruta': enlace, 
        'enviar': 'Enviar'
    })
    print ('Mandando Nombre: %s, Icono: %s, Enlace: %s' % (nombre, icono, enlace))