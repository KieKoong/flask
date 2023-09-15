from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    name = 'KieKoong'
    return render_template('index.html', name=name)

@app.route('/submitted', methods=['POST', 'GET'])
def submitted():
    name = request.form['name']
    surname = request.form['surname']
    return render_template('submitted.html', name=name, surname=surname)

if __name__ == '__main__':
    app.run(debug=True)