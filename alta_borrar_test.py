import requests, random, string

ip = 'localhost'
url = 'http://'+ip+'/Ejercicios/DWES/Repaso/ejerciciosServidor/3_Minijuegos_Juanma/app/php/index.php?accion=alta'
letras = string.ascii_letters + string.digits + '!@#$%^&*()'

for i in range(255):
    nombre = ''.join(random.choice(letras) for i in range(4))
    icono = ''.join(random.choice(letras))
    enlace = ''.join(random.choice(letras))
    requests.post(url, allow_redirects=False, data={
        'nombre': nombre,
        'icono': icono,
        'ruta': enlace, 
        'enviar': 'Enviar'
    })
    print ('Mandando Nombre: %s, Icono: %s, Enlace: %s' % (nombre, icono, enlace))


id = 0
while id < 255:
    id+=1
    strId = str(id)
    ip = 'localhost'
    url = 'http://'+ip+'/Ejercicios/DWES/Repaso/ejerciciosServidor/3_Minijuegos_Juanma/app/php/index.php?accion=borrar&id='+ strId

    requests.post(url, allow_redirects=False, data={
        'borrar': 'Borrar'
    })
    print ('Borrando minijuego con id: %i' % (id))