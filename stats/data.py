import os, glob

import pandas as pd

game_files = glob.glob(os.path.join(os.getcwd(), "games", "*.EVE"))

game_files.sort()

game_frames = []
for game_file in game_files:
    game_frame = pd.read_csv(
        game_file, names=["type", "multi2", "multi3", "multi4", "multi5", "multi6", "event"]
    )
    game_frames.append(game_frame)

games = pd.concat(game_frames)

games.loc[games["multi5"] == "??",] = ""

