# IMPORTS
import random
import neurokit2 as nk

# GLOBAL CONSTANTS

# FUNCTION DEFINITIONS

# CLASSES
class ecg_data:

    def __init__(self):
        self.ecg = 0
        self.signals = 0
        self.info = 0
        self.random_rate = 0
        self.heart_rate = []

    def generate_ecg(self):
        self.random_rate = random.randint(20, 200)
        self.ecg = nk.ecg_simulate(duration=15, sampling_rate=1000, heart_rate=self.random_rate)
        self.signals, self.info = nk.ecg_process(self.ecg, sampling_rate=1000)
        #print(self.info.keys()) - Debugging to find ECG_Rate which is changed
        #print(self.signals.keys())
        
        self.heart_rate = self.signals["ECG_Rate"]
        return self.heart_rate

# MAIN EXECUTION BLOCK
def main():
    
    Ecg = ecg_data()
    print(Ecg.generate_ecg())

# ENTRY POINT
if __name__ == '__main__':
    main()