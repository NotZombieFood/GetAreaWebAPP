# GetAreaWebAPP
Web app written in python (uses flask and opencv) that gets the area of an object. It need to get a fixed size image, like A4.

![Lenguaje](https://img.shields.io/badge/Lenguaje-Python-blue.svg)
[![Website](https://img.shields.io/badge/Website-Heroku-green.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAQAAAC1QeVaAAAA70lEQVQY013QPUuCYRiG4aclG5qlrVp1K9SIqFWlD0iwralyiFd8p0ptaMoaioRwKoTEJiEcKn/d0ZDax72ey30dIYQQQhAkFAwNFSSE6QlmpJ2riEQqzqXNGKekE5dy1vX0rMtoOJEUgkUDp2YVVcVqIrGUUwOLQVbHjSPLVnV1rdgxcq8jG6w5Vvag61VT04s7D8qOrX3HkrwL1z6NnNmSV/ofW969u1VXsP8Ty9qe9TXV9Tx5dPAdszrujWxbGT9U9KHlSm4yJSUWqYlFYmmH2pYmCA0ZG/pThIoFv/gubNpT/cM39Z0zb9fbb/gvvC7zcIQtJxIAAAAASUVORK5CYII=)](basiko.cloudapp.net:8080)
[![Requisitos](https://img.shields.io/badge/Requisitos-Actualizados-green.svg)](https://github.com/NotZombieFood/GetAreaWebAPP/blob/master/requirements.txt)

## Funciones / Notas
+ Form para subir imagen.
+ Saca la relación entre la cantidad de área de la imágen y después multiplica por el área de una hoja tamaño carta.
+ Heroku procfile pero con problema para poder usan opencv, recomiendo montar en server corriendo Ubuntu.



## ¿Cómo correrlo en local?
1. En caso de tener Python3, pip y virtual env; ir al paso 5.
2. Instalar Python3
3. Instalar pip 
4. Instalar virtualenv mediante "pip install virtualenv". 
5. Crear un virtual env mediante "mkvirtualenv metodos".
6. Ir al folder donde clonamos el repo y correr el siguiente comando "setprojectdir .", mediante esto cada vez que ingresemos al entorno se´redireccionará al folder. Para salir del entorno tenemos que usar "deactivate" y para regresar "workon InnoverAPI". Si todo funciona debería de salirnos **(InnoverAPI)** antes de nuestro cursor en la consola.
7. Correr "pip install -r requirements.txt"
8. Correr  "python3 app.py" o "python app.py"
9. En nuestra url local en el puerto 8080 se debería ver un el sitio.
