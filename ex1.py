from flask import Flask, render_template, url_for
app=Flask(__name__, static_url_path='/static')

@app.route('/', methods=['GET', 'POST'])
def ex1():
         
       return render_template('ex1.html')
    
if __name__ == '__main__':
     app.run()    
