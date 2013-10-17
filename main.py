from flask import Flask
from flask import render_template, request
from settings import appname 
from calculator import Calc

app = Flask(appname)

@app.route('/', methods=['GET', 'POST'])
def main():
    """
    The main section of the app that lets you pick parameters.
    It then parses the same display template as later on.
    """
    if request.method == 'POST':
        slength = request.form['p_count_field']
        stype = 'brute_force' #request.form.get('p_method')
    
        if int(slength) < 1:
            slength = 0
            results = {
                'result': [0],
                'error_msg': 'Number of primes to calculate must be > 0.'
            }
        else:
            results = get_results(stype, slength)
            
        context = {
            'stype': stype,
            'slength': slength,
            'res_list': results['result'],
            'error': results['error_msg']
        }
        template = 'display_results.html'
    else:
        template = 'main.html'
        context = {}
    return render_template(template, **context) 

def get_results(stype, slength):
    """
    Takes a type of search, and the number of primes wanted,
    and returns a list of integers.
    """
    # Give us an instance of the Calc class
    calc = Calc(slength)
    # The class will check for valid search type
    calc.run_method(stype)
    
    return {'error_msg': calc.errors, 'result': calc.result}

@app.route('/<stype>/<int:slength>')
def display_results(stype, slength):
    """
    Take GET data and display the results. This allows users to
    "hotwire" into the results page without any form submittal.
    """
    results = get_results(stype, slength)
    context = {
        'stype': stype, 
        'slength': slength,
        'res_list': results['result'],
        'error': results['error_msg'] 
    }
    return render_template('display_results.html', **context)

if __name__=='__main__':
    app.run(debug=True)

