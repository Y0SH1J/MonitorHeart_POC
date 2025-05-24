# IMPORTS
import random

# GLOBAL CONSTANTS

# FUNCTION DEFINITIONS

# CLASSES
class temperature_data:

    def __init__(self):
        self.temp = 0

    def generate_temp(self):
        self.temp = random.randint(50,110)
        return self.temp

# MAIN EXECUTION BLOCK
def main():
    
    Temp = temperature_data()
    print(Temp.generate_temp())

# ENTRY POINT
if __name__ == '__main__':
    main()