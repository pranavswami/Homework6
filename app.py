from flask import Flask, jsonify

app = Flask(__name__, static_folder='./frontend/build', static_url_path='/') 


@app.route('/name/Pranav')
def lastName():
    return jsonify(lastName = 'Swaminathan')

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run()