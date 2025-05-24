# IMPORTS

import ECG_Heart

import keyboard
import schedule #A simple to use API for scheduling jobs, made for humans
import time
from flask import Flask


# GLOBAL CONSTANTS

# FUNCTION DEFINITIONS

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Heart Rate Monitoring</h1>"

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
        self.parameter_check(120, 80, self.check_bpm, "Heart Rate")
        user.user1.append(self.check_bpm)

# MAIN EXECUTION BLOCK
def main():

    """Get continuous data from different devices"""
    users = user()
    sensors = sensors_interface()

    # If you want to pass arguments to the function then use the following:
    # import functools
    # schedule.every(5).seconds.do(functools.partial(sensors.Heart_check, arg1, arg2))
    # or
    # schedule.every(5).seconds.do(lambda: sensors.Heart_check(arg1, arg2))

    # You have to pass the function as a reference, not call it over here. Not sensors.Heart_check(), 
    # because this is passing the return value not the function
    # which is none in this case.
    
    users.create_user_list()
    sensors.scheduling(1, users)
    
    while True:

        schedule.run_pending()
        time.sleep(1)

        if keyboard.is_pressed('a'):
            print(users.user1)
            exit(0)
    

# ENTRY POINT
if __name__ == "__main__": # Whether certain code should run when the script is executed directly, versus when it is imported as a module into another script.
    main()




# Modules installed
# pip install keyboard
# pip install neurokit2 ; https://neuropsychology.github.io/NeuroKit/examples/ecg_delineate/ecg_delineate.html
# pip install Flask
# pip install PyWavelets
# pip install schedule