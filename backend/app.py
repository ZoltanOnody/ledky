import time

from flask import Flask, request, jsonify
from flask_cors import CORS
import pigpio


class Light:
    def __init__(self):
        self.rpi = pigpio.pi()
        self._PIN_r = 17
        self._PIN_R = 18
        self._PIN_B = 21
        self._PIN_POWER = 20
        self.rpi.set_mode(self._PIN_R, pigpio.OUTPUT)
        self.rpi.set_mode(self._PIN_R, pigpio.OUTPUT)
        self.rpi.set_mode(self._PIN_B, pigpio.OUTPUT)

        self.rpi.set_mode(self._PIN_POWER, pigpio.OUTPUT)

        self.rpi.set_PWM_dutycycle(self._PIN_R, 0)
        self.rpi.set_PWM_dutycycle(self._PIN_R, 0)
        self.rpi.set_PWM_dutycycle(self._PIN_B, 0)

        self.rpi.set_PWM_frequency(self._PIN_R, 200)
        self.rpi.set_PWM_frequency(self._PIN_R, 200)
        self.rpi.set_PWM_frequency(self._PIN_B, 200)

    def set(self, r, g, b):
        self.rpi.set_PWM_dutycycle(self._PIN_R, r)
        self.rpi.set_PWM_dutycycle(self._PIN_R, g)
        self.rpi.set_PWM_dutycycle(self._PIN_B, b)

    def get(self):
        r = self.rpi.get_PWM_dutycycle(self._PIN_R)
        g = self.rpi.get_PWM_dutycycle(self._PIN_R)
        b = self.rpi.get_PWM_dutycycle(self._PIN_B)
        return r, g, b

    def set_power(self):
        r, g, b = self.get()
        if r == g == b == 0:
            self.rpi.write(self._PIN_POWER, 0)
        else:
            self.rpi.write(self._PIN_POWER, 1)

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
