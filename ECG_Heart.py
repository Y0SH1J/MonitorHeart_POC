# IMPORTS
import random
import neurokit2 as nk
import wfdb # Waveform database from MIT

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
        self.record = wfdb.rdrecord('100', pn_dir='mitdb') # Download record '100' from PhysioNet
        self.fs = self.record.fs

    def generate_ecg(self, count):
        self.signals = self.record.p_signal[:self.fs*10, 0] # Plot first 10 seconds of lead 0
        # if count > len(self.signals):
        # self.signals = self.signals[:self.fs*10]
        self.heart_rate = self.signals[count]
        return self.heart_rate
    
    def generate_anomaly(self):
        
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