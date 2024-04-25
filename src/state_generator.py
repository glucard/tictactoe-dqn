from .tictactoe import TicTacToe
import copy, os
import json
from collections import Counter

def listOfActions():
    actions = []
    for i in range(3):
        for j in range(3):
            actions.append((j, i))
    return actions

class TictactocStates():
    def __init__(self):
        self.reset()

    def reset(self):
        self.actions = listOfActions()
        self.states = []
        game_start_state = TicTacToe()
        self.stateGenerator(game_start_state)
        for state in self.states:
            self.canWin(state)
        self.not_finished_states = [state for state in self.states
                                    if state['done'] == False]

    def find(self, game_state):
        """
        rotations_encoded = []
        for i in range(4):
            rotations_encoded.append(game_state.encode())
            game_state.rotate()

        id = 0
        for state in self.states: 
            id += 1
            for encoded in rotations_encoded:
                if state['encoded'] == encoded:
                    return True, state['id']
        return False, id
        """
        id = 0
        for state in self.states: 
            id += 1
            if state['encoded'] == game_state:
                return True, state['id']
        return False, id

    def canWin(self, state):
        wins = 0
        for next_state in [self.states[id] for id in state['actions']]:
            if next_state['done'] == True:
                if state['turn'] % 2 == 0:
                    wins += 1 if next_state['winner'] == 'x'else 0
                else:
                    wins += 1 if next_state['winner'] == 'o'else 0
        state['possible_wins'] = wins

    def stateGenerator(self, game_state):
        encoded = game_state.encode()
        exist, id = self.find(encoded)

        if id % 1_000 == 0:
            print(id)
            
        if not exist:
            done = not game_state.notFinished()
            state_element = {
                'id': id,
                'encoded': encoded,
                'actions': [],
                'done': done,
                'turn': game_state.turn_count,
                'winner': game_state.winner(),
            }
            self.states.append(state_element)
            if not done:
                for i in range(9):
                    next_state_game = copy.deepcopy(game_state)
                    action = id
                    if next_state_game.mark(self.actions[i][0], self.actions[i][1]):
                        action = self.stateGenerator(next_state_game)
                    state_element['actions'].append(action)
        return id

def generate_states():
    tstates = TictactocStates()
    if not os.path.exists("data"):
        os.mkdir("data")
    
    textfile = open("data/states.txt", "w")
    for element in tstates.states:
        textfile.write("id: " + str(element['id']) + "\n")
        textfile.write("encoded: " + element['encoded'] + "\n")
        textfile.write("actions: " + str(element['actions']) + "\n")
        textfile.write("possible_wins: " + str(element['possible_wins']) + "\n")
        textfile.write("done: " + str(element['done']) + "\n")
        textfile.write("turn: " + str(element['turn']) + "\n")
        textfile.write("winner: " + str(element['winner']) + "\n" + "\n")
    textfile.close()

    file_dict = {
        "states": tstates.states
    }
    
    with open("data/states.json", "w") as outfile: 
        json.dump(file_dict, outfile)


if __name__ == "__main__":
    generate_states()