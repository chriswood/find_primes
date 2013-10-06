from flask import Flask
from flask import render_template
from settings import appname 

app = Flask(appname)

@app.route('/')
def main():
    return 'in main!' 


def get_results(stype, slength):
    """
    Takes a type of search, and the number of primes wanted,
    and returns a list of integers.
    """
    return [1,2,3,5,7]


@app.route('/<stype>/<int:slength>', methods=['GET', 'POST'])
def display_results(stype, slength):
    """doc str"""
    #get the get vars type and length
    #instantiate
    #calculate
    #print results
    error_msg = 'ggg'
    results = range(100)
    if stype != 'default_method': #temp
        error_msg = 'Invalid or missing search type'
    context = {
        'stype': stype, 
        'slength': slength,
        'res_list': get_results(stype, slength),
        'error_msg': error_msg
    } 
    return render_template('display_results.html', **context)
    

if __name__=='__main__':
    app.run(debug=True)

