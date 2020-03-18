import flask
import flask_httpauth
import werkzeug.security as ws

import nest

app = flask.Flask(__name__)
auth = flask_httpauth.HTTPBasicAuth()

users = {
    "user": ws.generate_password_hash("user")
}


@auth.verify_password
def verify_password(username, password):
    if username in users:
        return ws.check_password_hash(users.get(username), password)
    return False


@app.route('/nest', methods=['POST'])
@auth.login_required
def nest_process():
    json_data = flask.request.get_json(force=True)
    nkeys = flask.request.args.get('nkeys')

    return flask.jsonify(nest.nest_json(json_data, nkeys.split(',')))


if __name__ == '__main__':
    app.run()
