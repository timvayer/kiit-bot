from flask import Flask, request
import subprocess
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return "Webhook is alive!", 200

@app.route("/webhook", methods=["POST"])
def webhook():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("bot.log", "a") as log:
        log.write(f"{now} — Отримано POST-запит від GitHub\n")
    subprocess.Popen(["/bin/bash", "deploy.sh"])
    return "OK", 200

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=80)

