from flask import Flask, request, jsonify

app = Flask(__name__)

# get echo api
@app.route('/echo_call/<param>')
def get_echo_call(param):
    return jsonify({"param": param})

@app.route('/Login', methods=["POST"])
def login():
    user = request.get_json()
    print(user)
    return jsonify(user)



if __name__ == "__main__":
    app.run(debug=True)