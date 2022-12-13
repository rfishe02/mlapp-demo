# mlapp-demo

There are various ways to deploy machine learning models, including the following popular tools:
- HTTP Servers such as Flask, Django, Apache OpenWhisk, and Python http.server.
- Cloud services such as Google Cloud ML, Azure ML, Amazon Sage Maker, and Algorithmia.
- Serving libraries such as TensorFlow Serving, NVIDIA TensorRT, DeepDetect, MXNet Model Serving, Skymind Intelligence Layer with DeepLearning4J, Seldon, and DeepStack AI Server.
- Cloud AI orchestration frameworks like KubeFlow.

Flask and cloud services are a great choice for small-scale projects. As an illustration, this repository will show how to use Flask to deploy a fine-tuned GPT-2 model.

# Sources
- Chapter 9. Scalable Inference Serving on Cloud with TensorFlow Serving and KubeFlow, Practical Deep Learning for Cloud, Mobile, and Edge by Anirudh Koul, Meher Kasam, and Siddha Ganju.
- Load pretrained instances with an AutoClass, Accessed at: https://huggingface.co/docs/transformers/autoclass_tutorial