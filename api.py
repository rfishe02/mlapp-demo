
from flask import Flask, render_template
from transformers import AutoTokenizer, AutoModelForCausalLM

app = Flask(__name__)

# Load the model from the directory.
model = AutoModelForCausalLM.from_pretrained('./model')

# Load the tokenizer from the directory.
tokenizer = AutoTokenizer.from_pretrained('./tokenizer')

@app.route("/")
def index():

    # Find the index.html file in the templates folder and serve it.
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    return "Not finished"

if __name__ == "__main__":
    app.run(debug=True)
