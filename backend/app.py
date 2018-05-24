import time

from flask import Flask, request, jsonify
from flask_cors import CORS
import pigpio


class Light:
    def __init__(self):
        self.rpi = pigpio.pi()
        self.pin_r = 17
        self.pin_g = 18
        self.pin_b = 21
        self.pin_power = 20
        self.rpi.set_mode(self.pin_r, pigpio.OUTPUT)
        self.rpi.set_mode(self.pin_g, pigpio.OUTPUT)
        self.rpi.set_mode(self.pin_b, pigpio.OUTPUT)
        
        self.rpi.set_mode(self.pin_power, pigpio.OUTPUT)    

        self.rpi.set_PWM_dutycycle(self.pin_r,0)
        self.rpi.set_PWM_dutycycle(self.pin_g,0)
        self.rpi.set_PWM_dutycycle(self.pin_b,0)
        
        self.rpi.set_PWM_frequency(self.pin_r,200)
        self.rpi.set_PWM_frequency(self.pin_g,200)
        self.rpi.set_PWM_frequency(self.pin_b,200)

    def set(self, r, g, b):
        self.rpi.set_PWM_dutycycle(self.pin_r, r)
        self.rpi.set_PWM_dutycycle(self.pin_g, g)
        self.rpi.set_PWM_dutycycle(self.pin_b, b)
                

    def get(self):
        r = self.rpi.get_PWM_dutycycle(self.pin_r)
        g = self.rpi.get_PWM_dutycycle(self.pin_g)
        b = self.rpi.get_PWM_dutycycle(self.pin_b)
        return r, g, b
    def set_power(self):
        r, g, b = self.get()
        if r == g == b == 0:
            self.rpi.write(self.pin_power,0)
        else:
            self.rpi.write(self.pin_power,1)

light = Light()
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.json
        light.set(r=content['r'], g=content['g'], b=content['b'])
        light.set_power()
    r, g, b = light.get()
    return jsonify({'r': r, 'g': g, 'b': b})
