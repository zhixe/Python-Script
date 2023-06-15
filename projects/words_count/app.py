from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for handling the form submission
@app.route('/count', methods=['POST'])
def count():
    # Get the form data
    count_with_spaces = request.form.get('count_with_spaces')
    word = request.form.get('word')

    # Count the word with or without spaces
    if count_with_spaces != "yes":
        # Remove spaces and tabs
        word = word.replace(" ", "").replace("\t", "")
    total_alphabets = len(word)

    # Render the result template with the output
    return render_template('result.html', total_alphabets=total_alphabets)

if __name__ == '__main__':
    app.debug = True
    app.run()

