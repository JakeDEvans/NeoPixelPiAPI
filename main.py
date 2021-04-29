from fastapi import FastAPI
from pydantic import BaseModel
import board, neopixel

class Item(BaseModel):
    led: int
    red: int
    green: int
    blue: int

#Define Variables
LED_COUNT=100

app = FastAPI()
pixels = neopixel.NeoPixel(board.D18, LED_COUNT)

@app.post('/json')
async def create_item(item: Item):
    pixels[item.led] = (item.red, item.green, item.blue)
    return item

@app.post('/color')
async def post_color(led: int, red: int, green: int, blue: int):
    pixels[led] = (red, green, blue)
    return {"Success": f"{led}, {red}, {green}, {blue}"}

@app.post('/clear')
async def clear_color():
    for i in range(LED_COUNT):
        pixels[i] = (0, 0, 0)

    return {"Success": "String Cleared"}
