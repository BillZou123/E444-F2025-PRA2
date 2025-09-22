from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment

from datetime import datetime

app = Flask(__name__)
Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    name = "Bill"   
    current_time = datetime.now()
    return render_template('mainpage.html', name=name, current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)