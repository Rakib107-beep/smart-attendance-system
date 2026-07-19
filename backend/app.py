from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Attendance Management System"

@app.route("/api/test")
def test():
    return jsonify({""
                    "status": "success",
                    "message": "Flast Api is Working"
                    })
if __name__ == "__main__":
    app.run(debug=True)
