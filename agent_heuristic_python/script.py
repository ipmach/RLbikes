from heuristics import heuristic_basic
import matplotlib.pyplot as plt
import numpy as np
import requests
import argparse
import json

# Parser options
parser = argparse.ArgumentParser()
parser.add_argument("--game", required=True)
parser.add_argument("--bike", required=True)
parser.add_argument('--debug', const=True, type=bool,
                    default=False,  nargs="?")
parser.add_argument("--ip", default="http://127.0.0.1:5000/")
parser.add_argument("--deterministic", const=True, type=bool,
                    default=False,  nargs="?")

# Parameters
game = int(parser.parse_args().game)
bike = int(parser.parse_args().bike)
debug = parser.parse_args().debug
IP = parser.parse_args().ip
deterministic = parser.parse_args().deterministic


# Join game
try:
    r = requests.get(IP + 'join/' + str(game))
    print(r)
except requests.exceptions.ConnectionError:
    print("Error: Unable to connect to IP " + IP)
    exit()

# Play game
Agent = heuristic_basic.BasicHeuristic(deterministic=deterministic)
view_size, mono, rotate = Agent.request_view()

timeStep = -1
move, speed = 0, 0

while True:

    if timeStep <= 0:  # First time
        params = json.dumps({"bike":bike, "range":view_size, "mono":mono, "rotate": rotate})
        r = requests.post(IP + '/view/bike/' + str(game), data=params)
    else:  # Rest
        try:
            params = json.dumps({"bike": bike, "range": view_size, "mono": mono, "rotate": rotate,
                                 "move": move, "speed": speed, "return": True})
            r = requests.post(IP + '/play/' + str(game), data=params)
        except TypeError as e:
            print(e)

    data_obtain = json.loads(r.text)

    # Stop the loop
    if data_obtain['Alive'] != 'alive' or data_obtain['Status'] == 'Finish':
        break

    timeStep = int(data_obtain['TimeStep'])
    idx_array = data_obtain['Board_view'][1:].split("  ")

    # Optain view
    view = np.zeros((view_size * 2 + 1, view_size * 2 + 1))
    for position in idx_array:
        try:
            aux = position.replace(" ", "").replace("(", "",).replace(")", ",")
            [x, y, value] = aux.split(",")
            view[int(x), int(y)] = float(value)
        except ValueError:
            pass

    print("TimeStep", timeStep)
    print(view)

    if debug:  # Debugger mode
        fig = plt.figure(1)
        plt.imshow(view)
        plt.draw()
        plt.pause(0.001)

    # Make move
    move, speed = Agent(view, timeStep)



