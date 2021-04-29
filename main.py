from fastapi import FastAPI
import board, neopixel

#Define Variables
LED_COUNT=100

app = FastAPI()
pixels = neopixel.NeoPixel(board.D18, LED_COUNT)

@app.post('/color')
async def post_color(led: int, red: int, green: int, blue: int):
    pixels[led] = (red, green, blue)
    return {"Success": f"{led}, {red}, {green}, {blue}"}

@app.post('/clear')
async def clear_color():
    for i in range(LED_COUNT):
        pixels[i] = (0, 0, 0)

    return {"Success": "String Cleared"}
