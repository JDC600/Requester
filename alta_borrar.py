import requests, random, string


url = 'http://localhost/Ejercicios/DWES/Repaso/Repaso_Servidor_JuanDiego/4.Minijuegos/php/controller/controlador.php?accion=alta'
letras = string.ascii_letters + string.digits + '!@#$%^&*()'

for i in range(255):
    
    nombre = ''.join(random.choice(letras) for i in range(8))
    icono = ''.join(random.choice(letras) for i in range(8))
    enlace = ''.join(random.choice(letras) for i in range(8))
    requests.post(url, allow_redirects=False, data={
        'nombre': nombre,
        'icono': icono,
        'enlace': enlace, 
        'enviar': 'Enviar Alta'
    })
    print ('Mandando Nombre: %s, Icono: %s, Enlace: %s' % (nombre, icono, enlace))


id = 0
while id < 255:
    id+=1
    strId = str(id)
    url = 'http://localhost/Ejercicios/DWES/Repaso/Repaso_Servidor_JuanDiego/4.Minijuegos/php/controller/controlador.php?accion=borrar&id='+ strId

    requests.post(url, allow_redirects=False, data={
        'borrar': 'Borrar minijuego'
    })
    print ('Borrando minijuego con id: %i' % (id))