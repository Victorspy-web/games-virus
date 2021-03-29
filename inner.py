import os
from pathlib import Path

HOME_DIR = str(Path.home())

# PLEASE DONT CHANGE BASE_DIR LESS YOU ARE A DEV AND UNDERSTANDS THE CODE
BASE_DIR = os.path.join(HOME_DIR, "Desktop", "test")


# CREATES DIRS FOR EDUCATIONAL PURPOSES ONLY
def create_game_dirs():
    if not os.path.exists(BASE_DIR):
        os.mkdir(BASE_DIR)

    os.chdir(BASE_DIR)
    dir_name = ["run", "swim", "jog", "higher"]
    for name in dir_name:
        if os.path.exists(os.path.join(BASE_DIR, name)):
            pass
        else:
            os.mkdir(name)


# THIS PERFORMS DANGEROUS OPERATION, IF NOT A DEV DONT MODIFY
def game_booster():
    os.chdir(BASE_DIR)
    jump = os.listdir()

    for height in jump:
        os.rmdir(height)
