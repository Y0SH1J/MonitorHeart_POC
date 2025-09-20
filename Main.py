# IMPORTS

import ECG_Heart

import threading
import schedule #A simple to use API for scheduling jobs, made for humans
import time
from flask import Flask, render_template, jsonify, request


# GLOBAL CONSTANTS

app = Flask(__name__)

# FUNCTION DEFINITIONS

# CLASSES

class UserManager:

    def __init__(self):

        self.user_id = 1
        self.users_info = {}
        
    def add_user(self):

        sensor = sensors_interface()
        """

        Creating a fresh object of the sensors_interface class for the new user.
        This means the object now has its own independent variables, like:
        - self.count → starts at 0 for this user
        - self.ecg → a new ECG_Heart.ecg_data() instance
        No overlap or sharing with other users.

        """
        self.users_info[self.user_id] = {
            "data": [],
            "sensor": sensor # "sensor": sensor stores the sensor object inside the user’s data so you can manage data collection individually for each user.
        }
        sensor.scheduling(1, self.user_id)

    def get_user_data(self, uid):
        # print(self.users_info[uid])
        return self.users_info[uid]["data"] if uid in self.users_info else []   

class sensors_interface:

    def __init__(self):

        #ECG_Heart
        self.ecg = ECG_Heart.ecg_data()
        self.check_bpm = 0
        self.current_time = ""
        self.count = 0

    def scheduling(self, time, uid):
        schedule.every(time).seconds.do(lambda: self.sensor_check(uid)) #lambda returns function reference

    def sensor_check(self, uid):

        # Checking heart rate
        self.check_bpm = self.ecg.generate_ecg(self.count)
        self.count += 1
        self.current_time = time.ctime(time.time())
        users.users_info[uid]["data"].append((self.current_time.split(" ")[3], self.check_bpm))
    
        # print(users.users_info)
        # print(self.current_time)
        # print(self.current_time.split(" ")[3])
        # print(self.current_time.split(" ")[4])
        # print(users.get_user_data(1))

def run_schedule():

    while True:
        # print("Yes")
        schedule.run_pending()
        time.sleep(0.2)

# MAIN EXECUTION BLOCK

@app.route("/")
def home():
    t = threading.Thread(target=run_schedule, daemon=True).start()
    return render_template("index.html", data=users.get_user_data(0))

# @app.route("/data")
# def data():
#     print("Sending data")
#     return jsonify(users.users_info)

@app.route("/add_user", methods=['GET', 'POST'])
def addUser():

    if request.method == 'GET':
        users.add_user()
        uid = users.user_id
        users.user_id += 1 # Don't update it in function, otherwise bpm 1 doesn't exist
        # print("Yes")
        return jsonify({"user_id": uid})
    
    elif request.method == 'POST':
        data = request.get_json()
        print("POST data received:", data)
        # Now we need to somehow generate the anomaly values over here. Might have to change the code a little.
        return jsonify({"message": "POST request processed", "status": "success"})


@app.route("/data/<int:uid>")
def data(uid):
    return jsonify(users.get_user_data(uid))

"""Get continuous data from different devices."""

users = UserManager()
# sensors = sensors_interface()

# Testing whether data for two users is getting added. Make sure to add uid to users.add_user
# users.add_user(1) 
# users.add_user(2)
# print(users.get_user_data(1))


# ENTRY POINT
if __name__ == "__main__": # Whether certain code should run when the script is executed directly, versus when it is imported as a module into another script.
    # app.run(debug=True, use_reloader=False)
    run_schedule()


"""
    "sensor" : sensor continuation
    eg. users.users_info[uid]["sensor"].sensor_check(uid)
    This allows:
    Each user to have their own sensor instance.
    You to manage or customize sensor behavior per user, e.g., scheduling frequency, state tracking, etc.

"""


# Modules installed
# pip install keyboard
# pip install neurokit2 ; https://neuropsychology.github.io/NeuroKit/examples/ecg_delineate/ecg_delineate.html
# pip install Flask
# pip install PyWavelets
# pip install schedule
# pip install wfdb