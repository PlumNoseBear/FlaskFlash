from flask import Flask, render_template, request, flash, redirect, url_for, session
import os
from tqdm import tqdm

app = Flask(__name__)
app.secret_key = "super_secret_key"
app.config['UPLOAD_PATH'] = 'static/files'

def upload_with_progress(file):
    chunk_size = 4096
    total_size = os.fstat(file.fileno()).st_size
    progress_bar = tqdm(total=total_size, unit='B', unit_scale=True)
    with open(os.path.join(app.config['UPLOAD_PATH'], file.filename), 'wb') as f:
        while True:
            data = file.stream.read(chunk_size)
            if not data:
                break
            f.write(data)
            progress_bar.update(len(data))
            progress = int((progress_bar.n / progress_bar.total) * 100)
            flash('Загрузка: {}%'.format(progress), 'progress')
    progress_bar.close()

    flash('Файл загружен', 'success')
    return redirect(url_for('upload_form'))

@app.route('/')
def upload_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filename = file.filename
        upload_with_progress(file)
        return redirect(url_for('upload_form'))
    else:
        flash('Не выбран файл', 'error')
        return redirect(request.url)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)