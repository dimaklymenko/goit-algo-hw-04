from colorama import Fore
import sys
from pathlib import Path

path = sys.argv[1]

parent_folder_path = Path(path)

def parse_folder(path):
    try:
        for element in path.iterdir():
            if element.is_dir():
                print(Fore.RED + f"Parse folder : This is folder - {element.name}")
                # parse_folder(element) -> рекурсія
            if element.is_file():
                print(Fore.GREEN + f"Parse folder : This is file - {element.name}")
    except Exception as e:
        print(f"{e} with file")            


parse_folder(parent_folder_path)


