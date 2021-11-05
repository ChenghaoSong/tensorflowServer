# tensorflowServer

## Env
CPU: INTEL Xeon CPU E5-2630 v3 @ 2.4GHz
Memory: 256 GB
Python: 3.7
Tensorflow: 2.2.0

## MNIST TEST RESULT
Test Object: 28 * 28 image
Test iter: 100000
Total cost time: 454.646s
Image type: black and white
Container number: 1

## Colab TEST RESULT
Test Object: 500 * 300 image
Test iter: 10000
Total cost time: 230.1s
Image type: RGB
Container number: 1
Code repo: https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/images/classification.ipynb#scrollTo=5fWToCqYMErH

## Tensorflow server
command:

"""
docker run -t --rm -p 8501:8501 -v "./tf_model:/models/state" -e MODEL_NAME=state tensorflow/serving &
"""
