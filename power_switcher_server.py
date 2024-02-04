from fastapi import FastAPI
import RPi.GPIO as GPIO

# GPIOピンの設定
GPIO_PIN = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.OUT)

app = FastAPI()

@app.get("/on")
def light_on():
    try:
        GPIO.output(GPIO_PIN, GPIO.HIGH)
        return {"message": "power on successed"}
    except:
        return {"message": "power on failed"}

@app.get("/off")
def light_off():
    try:
        GPIO.output(GPIO_PIN, GPIO.LOW)
        return {"message": "power off successed"}
    except:
        return {"message": "power off failed"}

@app.get("/status")
def light_status():
    try:
        status = GPIO.input(GPIO_PIN)
        return {"status": status}
    except:
        return {"message": "status failed"}