# IMPORTS
import random

# GLOBAL CONSTANTS

# FUNCTION DEFINITIONS

# CLASSES
class oxygen_data:

    def __init__(self):
        self.spo2 = 0

    def generate_spo2(self):
        self.spo2 = random.randint(60,150)
        return self.spo2

# MAIN EXECUTION BLOCK
def main():
    
    Spo2 = oxygen_data()
    print(Spo2.generate_bpm())

# ENTRY POINT
if __name__ == '__main__':
    main()