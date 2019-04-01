from flask import Flask
from flask import send_file
app = Flask(__name__)
usingPort = 5000
debugMode = True

@app.route('/down')
def downloadFile ():
    path = "./download/a.txt"
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    global usingPort, debugMode
    app.run(port=usingPort,debug=debugMode) 
