
import flask
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from keras.utils import img_to_array
from PIL import Image
import numpy as np
import io

app = flask.Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():

    return "Not finished"

if __name__ == "__main__":
    app.run(debug=True)
