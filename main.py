from flask import Flask
from flask import render_template
from settings import appname 
from calculator import Calc

app = Flask(appname)

@app.route('/')
def main():
    return 'in main!' 


def get_results(stype, slength):
    """
    Takes a type of search, and the number of primes wanted,
    and returns a list of integers.
    """
    # Give us an instance of the Calc class
    calc = Calc(slength)

    # The class will check for valid search type
    calc.run_method(stype)
    return calc.result  


@app.route('/<stype>/<int:slength>', methods=['GET', 'POST'])
def display_results(stype, slength):
    """
    Get needed data together for the search results page.
    I need to add error handling.
    """
    context = {
        'stype': stype, 
        'slength': slength,
        'res_list': get_results(stype, slength),
        'error_msg': '' 
    }
    return render_template('display_results.html', **context)
    

if __name__=='__main__':
    app.run(debug=True)

