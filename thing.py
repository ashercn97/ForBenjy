from flask import Flask, jsonify, request
import os


# from important_stuff import real_functionality
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './files/'


@app.route('/api/send', methods=['POST'])
def index():
    file = request.files['file']
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], "wow.png"))
    return jsonify({'result': 'success'})

def do_stuff(file):
    # do stuff
    # yay!
    return 'yay'



@app.route('/api/get_data', methods=['GET'])
def yay():
    output = do_stuff()
    return jsonify({'result': output})


if __name__ == '__main__':
    app.run(debug=True)
    




