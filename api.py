
# NOTE: A development server is not intended for use in production. 
# You will need to take additional steps to secure the application and improve its efficiency.
# See: https://flask.palletsprojects.com/en/2.2.x/tutorial/deploy/

from flask import Flask, render_template, request
from transformers import AutoTokenizer, AutoModelForCausalLM
import re

app = Flask(__name__)

# Load the fine tuned model saved at /model.
# If you haven't run the notebook, it will default to the pre-trained GPT-2 model.
try:
    model = AutoModelForCausalLM.from_pretrained('./model')
except:
    model = AutoModelForCausalLM.from_pretrained('gpt2')

# Load the tokenizer saved at /tokenizer.
# It will default to the original GPT-2 tokenizer.
try:
    tokenizer = AutoTokenizer.from_pretrained('./tokenizer')
except:
    tokenizer = AutoTokenizer.from_pretrained('gpt2')

@app.route("/")
def index():

    # Find the index.html file in the templates folder and serve it.
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    message = ""

    # Get the value of the input named prompt from the form data in the request object.
    start = request.form['prompt']

    if start is not None:
        if len(start) > 0:

            num_sequences =  5
            min_length =  50
            max_length =  100
            temperature = 0.75
            top_p = 0.95
            top_k = 75
            repetition_penalty =  1

            # Tokenize the prompt with our tokenizer.
            tokenized_prompt = tokenizer(start, return_tensors="pt")

            encoded_prompt = tokenized_prompt.input_ids.to(model.device)
            attention_mask = tokenized_prompt.attention_mask.to(model.device)

            # Create a series of predictions with our encoded prompt, attention mask, and other variables.
            output_sequences = model.generate(
                input_ids=encoded_prompt,
                attention_mask=attention_mask,
                max_length=max_length,
                min_length=min_length,
                temperature=float(temperature),
                top_p=float(top_p),
                top_k=int(top_k),
                do_sample=True,
                repetition_penalty=repetition_penalty,
                num_return_sequences=num_sequences)

            # Use the post_process function to clean up predictions, then append these to the outgoing message.
            for s in post_process(output_sequences):
                message += s + "<br><br>"

        else:
            message = "Prompt is too short."
    else:
        message = "Error retrieving form data."

    return {
        "message":message
    }

# Define a function that will decode the predictions and clean up the text for display purposes.
def post_process(output_sequences):
    generated_sequences = []
    predictions = []

    # Decode the prediction with the tokenizer.
    for generated_sequence_idx, generated_sequence in enumerate(output_sequences):
        generated_sequence = generated_sequence.tolist()
        text = tokenizer.decode(generated_sequence, clean_up_tokenization_spaces=True, skip_special_tokens=True)
        generated_sequences.append(text)

    # Loop over the decoded predictions and use regular expressions to clean up the data.
    for i, g in enumerate(generated_sequences):

        # Remove certain tokens like non ASCII characters, C0 controls, and some punctuation.
        res = re.sub(r'[^\u0000-\u007F]|[\u0000-\u0008\u000E-\u001F\u007F\u0022]',' ',str(g))

        # Replace multiple spaces with a single one.
        res = re.sub(r'[\u0009\u0020]+',' ',res)

        # Replace multiple newlines with a single one.
        res = re.sub(r'(\u0020*[\u000A-\u000D])+','<br>',res)

        predictions.append(res.strip())

    return predictions

if __name__ == "__main__":
    # NOTE: macOS Monterey introduced AirPlay Receiver running on port 5000. 
    # If you're using a Mac you'll have to use a different port to get localhost to resolve correctly.
    app.run(host='localhost', port=5050, debug=True)
