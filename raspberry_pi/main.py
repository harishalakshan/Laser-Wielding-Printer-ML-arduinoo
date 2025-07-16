
import serial
import numpy as np
import tensorflow as tf
import cv2

arduino = serial.Serial('/dev/ttyUSB0', 9600)
model = tf.keras.models.load_model('model.h5')

def preprocess_image(image):
    image = cv2.resize(image, (64, 64))
    image = image / 255.0
    return image

def predict_image(image):
    return model.predict(np.array([preprocess_image(image)]))

def send_laser_control(instructions):
    for cmd in instructions:
        arduino.write(f"{cmd},".encode())

image = cv2.imread('image.jpg')
prediction = predict_image(image)
laser_instructions = ["on", "off", "move_x", "move_y"]
send_laser_control(laser_instructions)
