from flask import Flask
from flask import render_template
from settings import appname 

app = Flask(appname)

@app.route('/')
def main():
    return 'in main!' 

@app.route('/results', methods=['GET', 'POST'])
def display_results(search_type='default_method'):
    error_msg = ''
    results = range(100)
    if search_type != 'default_method': #temp
        error_msg = 'Invalid or missing search type' 
    return render_template('display_results.html', method_name=search_type,
                               res_list=results, error_msg = error_msg)
    

if __name__=='__main__':
    app.run(debug=True)

