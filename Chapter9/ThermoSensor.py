#ThermoSensor
#Read input from thermister and modulate LED brightness

import RPi.GPIO as GPIO
import time, math

C = 0.33 # uF
R1 = 1000 # Ohms

GPIO.setmode(GPIO.BCM)

# Pin a charges the capacitor through a fixed 1k resistor and the thermistor in$
# pin b discharges the capacitor through a fixed 1k resistor 
a_pin = 18
b_pin = 23

#led_pin is for output
led_pin = 21
GPIO.setup(led_pin, GPIO.OUT)
pwm_led = GPIO.PWM(led_pin, 500)
pwm_led.start(0)


# empty the capacitor ready to start filling it up
def discharge():
    GPIO.setup(a_pin, GPIO.IN)
    GPIO.setup(b_pin, GPIO.OUT)
    GPIO.output(b_pin, False)
    time.sleep(0.01)
    
# return the time taken (uS) for the voltage on the capacitor to count as HIGH
# than means around 1.65V
def charge_time():
    GPIO.setup(b_pin, GPIO.IN)
    GPIO.setup(a_pin, GPIO.OUT)
    GPIO.output(a_pin, True)
    t1 = time.time()
    while not GPIO.input(b_pin):
        pass
    t2 = time.time()
    return (t2 - t1) * 1000000

# Take an analog reading as the time taken to charge after first discharging th$
def analog_read():
    discharge()
    t = charge_time()
    discharge()
    return t

# convert resistance to a duty cycle
def convert_to_duty(r):
    max_res = 1000
    min_res = 400
    duty = max((r-400,0)) # baseline it
    duty = int(100*duty / (max_res-min_res)) # scale it
    duty = 100 - duty # make brighter when warmer
    if (duty > 100):
        duty = 100
    if (duty < 0):
        duty = 0 # avoid out of bounds errors
    return duty
    
# To reduce errors, do it n times and take the average.
def read_resistance():
    n = 20
    total = 0;
    for i in range(1, n):
        total = total + analog_read()
    t = total / float(n)
    T = t * 0.632 * 3.3
    r = (T / C) - R1
    return r


try:
    while True:
        r = read_resistance()
        d = convert_to_duty(r)
        print(r)
        print(d)
        print()
        pwm_led.ChangeDutyCycle(d)
        time.sleep(0.1)
finally:  
    print("Cleaning up")
    GPIO.cleanup()
