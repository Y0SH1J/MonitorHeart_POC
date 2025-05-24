# IMPORTS
import random

# GLOBAL CONSTANTS

# FUNCTION DEFINITIONS

# CLASSES
class heart_data:

    def __init__(self):
        self.bpm = 0

    def generate_bpm(self):
        self.bpm = random.randint(0,300)
        return self.bpm

# MAIN EXECUTION BLOCK
def main():
    
    Bpm = heart_data()
    print(Bpm.generate_bpm())

# ENTRY POINT
if __name__ == '__main__':
    main()