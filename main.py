from flask import Flask, flash, redirect, render_template, request, url_for
import time

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        flash('Button was clicked!')
        time.sleep(1)  # Задержка в 1 секунду
        return redirect(url_for('index'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run()