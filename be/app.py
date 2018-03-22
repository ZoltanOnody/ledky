import time

from flask import Flask, request, jsonify
from flask_cors import CORS
import pigpio


class Light:
    def __init__(self):
        self.rpi = pigpio.pi()

        self.rpi.set_mode(17, pigpio.OUTPUT)
        self.rpi.set_mode(18, pigpio.OUTPUT)
        self.rpi.set_mode(21, pigpio.OUTPUT)

        self.rpi.set_mode(22, pigpio.OUTPUT)

        self.rpi.set_PWM_dutycycle(17,0)
        self.rpi.set_PWM_dutycycle(18,0)
        self.rpi.set_PWM_dutycycle(21,0)
        self.rpi.set_PWM_dutycycle(22,0)

        self.rpi.set_PWM_frequency(17,200)
        self.rpi.set_PWM_frequency(18,200)
        self.rpi.set_PWM_frequency(21,200)
        self.rpi.set_PWM_frequency(22,1)

    def set(self, r, g, b):
        self.rpi.set_PWM_dutycycle(17, r)
        self.rpi.set_PWM_dutycycle(18, g)
        self.rpi.set_PWM_dutycycle(21, b)

    def get(self):
        r = self.rpi.get_PWM_dutycycle(17)
        g = self.rpi.get_PWM_dutycycle(18)
        b = self.rpi.get_PWM_dutycycle(21)
        return r, g, b


light = Light()
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.json
        light.set(r=content['r'], g=content['g'], b=content['b'])

    r, g, b = light.get()
    return jsonify({'r': r, 'g': g, 'b': b})
