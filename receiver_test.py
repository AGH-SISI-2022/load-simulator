from flask import Flask, request

app = Flask(__name__)

@app.route('/send', methods=["POST"])
def send_video():
    print(request.get_data())

    return 'received send video'

@app.route('/watch', methods=["POST"])
def watch_video():
    print(request.get_data())

    return 'received watch video'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)