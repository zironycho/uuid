from flask import Flask, jsonify, abort
import uuid
import os

app = Flask(__name__)


_data_root = '/data'

@app.route('/')
def create_uuid():
    my_uuid = str(uuid.uuid4())
    path = os.path.join(_data_root, my_uuid)
    with open(path, 'w') as f:
        pass

    return jsonify({'uuid': my_uuid})

@app.route('/<my_uuid>')
def get_uuid(my_uuid):
    if os.path.exists(os.path.join(_data_root, my_uuid)):
        return jsonify({'exist':'yes'})
    else:
        return jsonify({'exist':'no'})


if __name__ == '__main__':
    app.run()
