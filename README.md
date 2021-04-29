# NeoPixelPiAPI
NeoPixel API for Raspberry Pi, useful for integrating with other systems.

## Startup
```
openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout server.key -out server.crt
sudo uvicorn --host 0.0.0.0 --port 8443 --ssl-certfile ./server.crt --ssl-keyfile ./server.key   main:app
```

## Test

### set led 0 to red, led 1 to green, led 3 to blue
```
curl -k -X POST https://localhost:8443/color?led=0\&red=255\&green=0\&blue=0
curl -k -X POST https://localhost:8443/color?led=1\&red=0\&green=255\&blue=0
curl -k -X POST https://localhost:8443/color?led=2\&red=0\&green=0\&blue=255
```

### clear all LEDs
```
curl -k -X POST https://localhost:8443/clear
```


### set led 9 to white using json
```
curl -k -X POST -d '{"led":9,"red":255,"green":255,"blue":255}' -H 'Content-Type: application/json'  https://localhost:8443/json
```
