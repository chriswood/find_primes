from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main():
    return 'in main!' 

@app.route('/results', methods=['GET', 'POST'])
def display_results(result_len=100, search_type='default_method'):
    results = range(len)
    if search_type == 'default_method':
        return render_template('display_results.html', method_name=search_type, res_list=results)
    else:
        error_msg = 'Invalid or missing search type' 

if __name__=='__main__':
    app.run(debug=True)

