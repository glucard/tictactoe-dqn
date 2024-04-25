import os
from .state_generator import generate_states

def main():
    print("working")
    
    if not os.path.exists("data/states.json"):
        generate_states()

if __name__ == "__main__":
    main()