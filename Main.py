# IMPORTS

import ECG_Heart

import threading
import schedule #A simple to use API for scheduling jobs, made for humans
import time
from flask import Flask, render_template, jsonify


# GLOBAL CONSTANTS

app = Flask(__name__)

# FUNCTION DEFINITIONS

# CLASSES

class UserManager:

    def __init__(self):

        self.user_id = 1
        self.users_info = {}
        
    def add_user(self):

        self.users_info[self.user_id] = []
        sensors.scheduling(1, self.user_id)
        self.user_id += 1

    def get_user_data(self, uid):
        # print(self.users_info[uid])
        return self.users_info[uid] if uid in self.users_info else []
    


class sensors_interface:

    def __init__(self):

        #ECG_Heart
        self.ecg = ECG_Heart.ecg_data()
        self.check_ecg = []
        self.check_bpm = 0

    def scheduling(self, time, uid):
        schedule.every(time).seconds.do(lambda: self.sensor_check(uid)) #lambda returns function reference

    def sensor_check(self, uid):

        # Checking heart rate
        self.check_ecg = self.ecg.generate_ecg()
        self.check_bpm = int(self.check_ecg[0])
        users.users_info[uid].append(self.check_bpm)
        
        # print(users.users_info)
        # print(users.get_user_data(1))

def run_schedule():

    while True:
        # print("Yes")
        schedule.run_pending()
        time.sleep(1)

# MAIN EXECUTION BLOCK

@app.route("/")
def home():
    t = threading.Thread(target=run_schedule, daemon=True).start()
    return render_template("index.html", data=users.get_user_data)

# @app.route("/data")
# def data():
#     print("Sending data")
#     return jsonify(users.users_info)

@app.route("/add_user")
def addUser():
    users.add_user()
    uid = users.user_id
    # print("Yes")
    return jsonify({"user_id": uid})

@app.route("/data/<int:uid>")
def data(uid):
    return jsonify(users.get_user_data(uid))

"""Get continuous data from different devices."""

users = UserManager()
sensors = sensors_interface()

# Testing whether data for two users is getting added. Make sure to add uid to users.add_user
# users.add_user(1) 
# users.add_user(2)
# print(users.get_user_data(1))


# ENTRY POINT
if __name__ == "__main__": # Whether certain code should run when the script is executed directly, versus when it is imported as a module into another script.
    # app.run(debug=True, use_reloader=False)
    run_schedule()




# Modules installed
# pip install keyboard
# pip install neurokit2 ; https://neuropsychology.github.io/NeuroKit/examples/ecg_delineate/ecg_delineate.html
# pip install Flask
# pip install PyWavelets
# pip install schedule