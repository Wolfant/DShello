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
