# Advanced-Webapp
Playing around with technologies building advanced webapps

## Project goal

Building a responsive web-app for monitoring and controlling the lamps in the class at the VUB.

## Project description

See report and API-docu in docu folder.

## Deploy project

1. Clone this repo 
```
git clone <repo>
```
2. Install docker 
3. Build image 
```
sudo docker build -t lamp-webapp:v1 .
```
4. Run container 
```
sudo docker run --name lampController -it --rm --network=host lamp-webapp:v1
```
5. Control the lamps (be sure to be connected with openvpn to the network before /!\ )

## Credits

Master course at the VUB, professor Kris Steenhaut & assistent Steffen Thielemans