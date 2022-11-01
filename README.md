# Advanced-Webapp
Playing around with technologies building advanced webapps

## Project goal

Building a responsive web-app for monitoring and controlling the lamps in the class at the VUB.

## Project description

...zolertia...coap...flask...hashing...websockets...docker...

## Deploy project

1. Clone this repo 
```
git clone <repo>
```
2. Install docker 
3. Build image 
```
sudo docker build -t lamp-webapp:v0 .
```
4. Run container 
```
sudo docker run --name lampController -it --rm --network=host lamp-webapp:v0
```
5. Control the lamps (be sure to be connected with openvpn before /!\ )

## Credits

Master course at the VUB, professor Kris Steenhaut & assistent Steffen Thielemans