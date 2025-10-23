import pickle
import base64
from flask import Flask, request
app = Flask(__name__)
@app.route("/vulnerable", methods=["POST"])
def vulnerableapp():
	form_data = base64.urlsafe_b64decode(request.form['hack'])
	deserialized = pickle.loads(form_data)
	return 'deserialized', 204
if __name__ == '__main__':
    print("Server is running at http://127.0.0.1:5000")
    app.run(port=5000)
