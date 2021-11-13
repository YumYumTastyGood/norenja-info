from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('location_m.html')
    
@app.route('/location')
def Index1():
    return render_template('location.html')

if __name__=='__main__':
    app.run()