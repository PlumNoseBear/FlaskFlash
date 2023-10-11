from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return '''
        <script>
            setTimeout(function() {
                alert('Button was clicked!');
            }, 1000);
            window.location.href = '/';
        </script>
        '''
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
