# mlapp-demo

There are various ways to deploy machine learning models, including the following popular tools:
- HTTP Servers such as Flask, Django, Apache OpenWhisk, and Python http.server.
- Cloud services such as Google Cloud AutoML, Azure ML, Amazon Sage Maker, and Algorithmia (acquired by DataRobot).
- Serving libraries such as TensorFlow Serving, NVIDIA TensorRT, DeepDetect, Apache MXNet, Skymind Intelligence Layer, Seldon, and DeepStack AI Server.
- Cloud AI orchestration frameworks like KubeFlow.

Flask and cloud services are great choices for small-scale projects. As an illustration, this repository shows how to use Flask to deploy a fine-tuned GPT-2 model.

First, run the cells in model.ipynb to fine tune a pre-trained GPT-2 model from Huggingface and save it. Then, run api.py to serve the saved model.

# Sources
- Chapter 9. Scalable Inference Serving on Cloud with TensorFlow Serving and KubeFlow, Practical Deep Learning for Cloud, Mobile, and Edge by Anirudh Koul, Meher Kasam, and Siddha Ganju.
- Code for Chapter 9: Scalable Inference Serving on Cloud with TensorFlow Serving and KubeFlow, Accessed at: https://github.com/PracticalDL/Practical-Deep-Learning-Book/tree/master/code/chapter-9
- Load pretrained instances with an AutoClass, Accessed at: https://huggingface.co/docs/transformers/autoclass_tutorial
- Quickstart - Flask Documentation (2.2.x), Accessed at: https://flask.palletsprojects.com/en/2.2.x/quickstart/
- JavaScript Cookbook by Adam D. Scott, Matthew MacDonald & Shelley Powers