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

class user:

    def __init__(self):

        #Dummy user 1
        self.user_id_1 = 1
        
    def create_user_list(self):

        #Dummy user 1
        self.user1 = [self.user_id_1]

class sensors_interface:

    def __init__(self):

        #ECG_Heart
        self.ecg = ECG_Heart.ecg_data()
        self.check_ecg = []
        self.check_bpm = 0

    def scheduling(self, time, user):
        schedule.every(time).seconds.do(lambda: self.sensor_check(time, user)) #lambda returns function reference

    def parameter_check(self, max, min, para, type):
        if para < min:
            print(f"{para}: Warning! {type} lowering!!")
        elif self.check_bpm > max:
            print(f"{para}: Warning! {type} too high!!")
        else:
            print(f"{para}: {type} Normal.")


    def sensor_check(self, time, user):

        # Checking heart rate
        self.check_ecg = self.ecg.generate_ecg()
        self.check_bpm = int(self.check_ecg[0])
        #self.parameter_check(120, 80, self.check_bpm, "Heart Rate")
        users.user1.append(self.check_bpm)
        print(users.user1)

def run_schedule():

    while True:
        print("Yes")
        schedule.run_pending()
        time.sleep(1)

# MAIN EXECUTION BLOCK

@app.route("/")
def home():
    t = threading.Thread(target=run_schedule, daemon=True).start()
    return render_template("index.html", data=users.user1)

@app.route("/data")
def data():
    print("Sending data")
    return jsonify(users.user1)

"""Get continuous data from different devices."""

users = user()
sensors = sensors_interface()
users.create_user_list()
sensors.scheduling(1, users)

# ENTRY POINT
if __name__ == "__main__": # Whether certain code should run when the script is executed directly, versus when it is imported as a module into another script.
    app.run(debug=True, use_reloader=False)
    # run_schedule()




# Modules installed
# pip install keyboard
# pip install neurokit2 ; https://neuropsychology.github.io/NeuroKit/examples/ecg_delineate/ecg_delineate.html
# pip install Flask
# pip install PyWavelets
# pip install schedule