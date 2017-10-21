# Informe Experto IT + DEVOPS

## Creación de Aplicacion

La aplicacione se creo siguiendo TDD con Python y Flask 



# DShello
Prueba DS

Auto Deploy on Heroku

https://devsu-tst.herokuapp.com/hello/{name}


## Google cloud

Se activa Tools -> Container Registry

sudo docker build -t "wolfant/devsu-nginx" .
sudo docker build -t "wolfant/devsu-app" .

sudo docker tag wolfant/devsu-app  'us.gcr.io/simplerest-183605/devsu-hello'
sudo docker tag wolfant/devsu-nginx  'us.gcr.io/simplerest-183605/devsu-nginx'

sudo gcloud auth login
sudo gcloud docker -- push us.gcr.io/simplerest-183605/devsu-nginx
sudo gcloud docker -- push us.gcr.io/simplerest-183605/devsu-hello

## Despliegue en google cloud
gcloud app deploy app.yaml --project simplerest-183605
https://simplerest-183605.appspot.com
[Test_app]

https://8080-dot-3171646-dot-devshell.appspot.com/hello/pepe
[Prod]
https://simplerest-183605.appspot.com/hello/example
