import requests, os, random, string, json


id = 0
while True:
    id+=1
    strId = str(id)
    url = 'http://localhost/Ejercicios/DWES/Repaso/Repaso_Servidor_JuanDiego/4.Minijuegos/php/controller/controlador.php?accion=borrar&id='+ strId

    requests.post(url, allow_redirects=False, data={
        'borrar': 'Borrar minijuego'
    })
    print ('Borrando minijuego con id: %i' % (id))

