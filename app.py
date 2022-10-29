from flask import Flask, render_template, jsonify

import receiver

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/logs")
def view_logs():
    logs = receiver.get_logs()
    return jsonify(logs)


@app.route("/robot-position")
def robot_position():
    position = receiver.get_robot_position()
    return jsonify({"x": position[0], "y": position[1]})


if __name__ == "__main__":
    app.run(port=5000, debug=True)
