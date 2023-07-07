# Import necessary libraries
import RPi.GPIO as GPIO
import time
from adafruit_servokit import ServoKit
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Clear display.
disp.fill(0)
disp.show()

# Create blank image for drawing.
width = disp.width
height = disp.height
image = Image.new("1", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

# Draw some text.
font = ImageFont.load_default()
total_spaces = 100  # Define total parking spaces
draw.text((0, 0), "Spaces: " + str(total_spaces), font=font, fill=255)

# Display image.
disp.image(image)
disp.show()

# Set the servo kit
kit = ServoKit(channels=16)

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the pins for the IR sensors and servo motors
IR_sensor_entrance = 14
IR_sensor_exit = 15
servo_motor_entrance = 0
servo_motor_exit = 1

# Set the IR sensor pins as input
GPIO.setup(IR_sensor_entrance, GPIO.IN)
GPIO.setup(IR_sensor_exit, GPIO.IN)

while True:
    # Check the entrance IR sensor
    if GPIO.input(IR_sensor_entrance):
        if total_spaces > 0:
            # Car detected, turn the servo motor
            kit.servo[servo_motor_entrance].angle = 90
            time.sleep(1)
            kit.servo[servo_motor_entrance].angle = 0
            total_spaces -= 1  # Decrease the number of available spaces
            draw.rectangle((0, 0, width, height), outline=0, fill=0)
            draw.text((0, 0), "Spaces: " + str(total_spaces), font=font, fill=255)
            disp.image(image)
            disp.show()
        else:
            # Car park is full
            draw.rectangle((0, 0, width, height), outline=0, fill=0)
            draw.text((0, 0), "FULL", font=font, fill=255)
            disp.image(image)
            disp.show()

    # Check the exit IR sensor
    if GPIO.input(IR_sensor_exit):
        # Car detected, turn the servo motor
        kit.servo[servo_motor_exit].angle = 90
        time.sleep(1)
        kit.servo[servo_motor_exit].angle = 0
        total_spaces += 1  # Increase the number of available spaces
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((0, 0), "Spaces: " + str(total_spaces), font=font, fill=255)
        disp.image(image)
        disp.show()

    time.sleep(0.1)  # Delay to avoid rapid sensor triggering

