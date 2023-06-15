from flask import Flask, render_template, request

app = Flask(__name__)

class WordCounter:
    def __init__(self, word, count_with_spaces, count_type):
        self.word = word
        self.count_with_spaces = count_with_spaces
        self.count_type = count_type

    def count_words(self):
        if self.count_with_spaces == "no":
            if self.count_type == "column":
                word_list = self.word.split()
                return len(word_list)
            elif self.count_type == "row":
                lines = self.word.split('\n')
                return sum(len(line.split()) > 0 for line in lines)
        elif self.count_type == "column":
            return len(self.word)
        elif self.count_type == "row":
            lines = self.word.split('\n')
            return len(lines)

        return 0

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for handling the form submission
@app.route('/count', methods=['POST'])
def count():
    # Get the form data
    count_with_spaces = request.form.get('count_with_spaces')
    count_type = request.form.get('count_type')
    word = request.form.get('word')

    counter = WordCounter(word, count_with_spaces, count_type)
    total_count = counter.count_words()

    # Render the result template with the output
    return render_template('result.html', total_count=total_count)

if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
