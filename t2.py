# -*- coding: utf-8 -*-
import json
from time import *
import requests
import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import tensorflow as tf
batch_size = 32
img_height = 180
img_width = 180

sunflower_url = "./1.jpg"
sunflower_path = tf.keras.utils.get_file('Red_sunflower', origin=sunflower_url)

img = load_img(
    sunflower_path, target_size=(img_height, img_width)
)
img_array = img_to_array(img).tolist()
print(img_array)
# img_array = tf.expand_dims(img_array, 0) # Create a batch

data = json.dumps({"signature_name": "serving_default", "instances": img_array})

headers = {"content-type": "application/json"}
sumt = 0
for i in range(10000):
    st = time()
    json_response = requests.post('http://172.169.8.5:8501/v1/models/state:predict',
                                  data=data, headers=headers)
    # predictions = json.loads(json_response.text)
    # predictions = np.array(predictions)
    # predictions = np.round(predictions)
    # state_curr = predictions[0]
    et = time()
    sumt += et - st

print(sumt)