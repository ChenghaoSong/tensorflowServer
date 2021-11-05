import json
from time import *
import paramiko
import requests
import numpy as np
import pandas as pd

import tensorflow as tf

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

s = x_train[0]

# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname='172.20.110.72', port=22, username='root', password='1212')
data = json.dumps({"signature_name": "serving_default", "instances": s})

headers = {"content-type": "application/json"}
sumt = 0
for i in range(10000):
    st = time()
    json_response = requests.post('http://localhost:8501/v1/models/state:predict',
                                  data=data, headers=headers)
    predictions = json.loads(json_response.text)["predictions"]
    predictions = np.array(predictions)
    predictions = np.round(predictions)
    state_curr = predictions[0]
    et = time()
    sumt += et - st

print(sumt)