from flask import Flask, render_template

import receiver

app = Flask(__name__)


@app.route("/logs")
def view_logs():
    logs = receiver.get_logs()
    return render_template("view_logs.html", logs=logs)
