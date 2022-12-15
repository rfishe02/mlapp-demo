# mlapp-demo

There are various ways to deploy machine learning models, including the following popular tools:
- HTTP Servers such as Flask, Django, Apache OpenWhisk, and Python http.server.
- Cloud services such as Google Cloud AutoML, Azure ML, Amazon Sage Maker, and Algorithmia (acquired by DataRobot).
- Serving libraries such as TensorFlow Serving, NVIDIA TensorRT, DeepDetect, Apache MXNet, Skymind Intelligence Layer, Seldon, and DeepStack AI Server.
- Cloud AI orchestration frameworks like KubeFlow.

As an illustration, this repository shows how to use Flask to deploy a fine-tuned GPT-2 model. First, run the cells in `model.ipynb` to fine tune a pre-trained GPT-2 model from Huggingface and save it. Then, run `api.py` to serve the saved model.

## Project Structure

### `model.ipynb`

A Jupyter notebook file that fine tunes a pre-trained GPT-2 model from Huggingface. It also saves the fine tuned model to a directory. It’s possible to put everything in the Flask application, but if we separate the model training from the Flask application it becomes easier to update the model independently of the Flask application. 

### `/templates/index.html`

A web interface for the application. It has a form with a text input and a button that will submit the form to the `/predict` endpoint of the Flask application.

### `api.py`

A Flask application that loads a saved model and tokenizer. It has a method  `index` that serves `/templates/index.html` and a method `predict` that uses the model to generate predictions.

# Sources
- Chapter 9: Scalable Inference Serving on Cloud with TensorFlow Serving and KubeFlow, Practical Deep Learning for Cloud, Mobile, and Edge by Anirudh Koul, Meher Kasam, and Siddha Ganju.
- Code for Chapter 9: Scalable Inference Serving on Cloud with TensorFlow Serving and KubeFlow, Accessed at: https://github.com/PracticalDL/Practical-Deep-Learning-Book/tree/master/code/chapter-9
- Load pretrained instances with an AutoClass, Accessed at: https://huggingface.co/docs/transformers/autoclass_tutorial
- Quickstart - Flask Documentation (2.2.x), Accessed at: https://flask.palletsprojects.com/en/2.2.x/quickstart/
- Get started with Bootstrap - Bootstrap v5.2, Accessed at: https://getbootstrap.com/docs/5.2/getting-started/introduction/
- Chapter 13: Fetching Remote Data, JavaScript Cookbook by Adam D. Scott, Matthew MacDonald & Shelley Powers