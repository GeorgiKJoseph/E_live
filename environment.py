import os

# BASE_DIR = /home/user/location_of_elive_folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# returns BASE_DIR
def getBaseDir():
    return BASE_DIR
