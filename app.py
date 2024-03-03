from flask import Flask, render_template, request
import re
#\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    
    matches = re.findall(regex_pattern, test_string)
    
    return render_template('result.html', test_string=test_string, regex_pattern=regex_pattern, matches=matches)

if __name__ == '__main__':
    app.run(debug=True)
