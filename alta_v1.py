import requests, json


url = 'http://localhost/Ejercicios/DWES/Repaso/Repaso_Servidor_JuanDiego/4.Minijuegos/php/controller/controlador.php?accion=alta'

datos = json.loads(open('data.json').read())

for dato in datos:
    requests.post(url, allow_redirects=False, data={
        'nombre': dato,
        'icono': dato,
        'enlace': dato,
        'enviar': 'Enviar Alta'
    })

    print ('Mandando Nombre: %s, Icono: %s, Enlace: %s' % (dato, dato, dato))

