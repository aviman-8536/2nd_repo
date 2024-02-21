from flask import Flask, request

app = Flask(__name__)

@app.route('/square', methods=['GET','POST'])
def square():
    if(request.method =="POST"):
        number = request.data
        result = number ** 2
        return {'result': result}
    return {"status":200}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080", debug=True)