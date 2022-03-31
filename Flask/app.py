import json
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# HOME 
@app.route('/home')
def home():
    return render_template('index.html')

# GET Request -> Pass user_name, pw to 'login.html'
@app.route('/board', methods=["GET", "POST"])
def board_list2():
    user_name = request.args.get('user_name')
    pw = request.args.get('pw')
    return render_template('login.html', user_name=user_name, pw=pw)
    
@app.route('/list')
def list():
    value_list = ['juhyun','lee', 'liljoo']
    return render_template('list.html', value_list = value_list)

@app.route('/double', methods=["GET", "POST"])
def double():
    if request.method == "GET":
        return F"GET 요쳥 내용은 {request.args.get('question')}"
        
    elif request.method == "POST":
        return F"POST 요청 내용은 {json.loads(request.get_data())}"

if __name__ == "__main__":
    app.run(debug=True)