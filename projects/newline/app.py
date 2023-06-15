from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for handling the form submission
@app.route('/create_newline', methods=['POST'])
def create_newline():
    # Get the form data
    word = request.form.get('word')

    # Split the word into a list of words
    word_list = word.split()

    # Create a newline-separated string
    word_with_newlines = "\n".join(word_list)

    # Render the result template with the output
    return render_template('result.html', word_with_newlines=word_with_newlines)

if __name__ == '__main__':
    app.debug = True
    app.run()

