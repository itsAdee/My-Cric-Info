import sys
import os
from pathlib import Path


def FindParticularMatches():
    currentPath = Path.cwd()
    match_directory = currentPath / "Matches"
    for file in os.listdir(match_directory):
        if file.endswith(".json"):
            print(file)


FindParticularMatches()
