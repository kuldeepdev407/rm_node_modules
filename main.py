import os
import argparse
import shutil

all_node_path = []
block_path = ['$RECYCLE.BIN','System Volume Information']



def getNodeModulesPaths(path):    
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_dir():
                    if(entry.name == 'node_modules'):
                        all_node_path.append(entry.path)
                    elif(entry.name in block_path):
                        continue
                    else:
                        getNodeModulesPaths(path+'/'+entry.name)
        return 1
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def remove_directory(directory_path):
    try:
        shutil.rmtree(directory_path)
        print(f"'{directory_path}' removed successfully.")
    except OSError as e:
        print(f"Error: {directory_path} : {e.strerror}")
def main():
    # arguments
    args_parser = argparse.ArgumentParser(description="CLI tool for removing all node_module folder for given path")
    args_parser.add_argument('-p', '--path', required=True, type=str,help="full path from where you want to remove node_module ")

    args = args_parser.parse_args()
    getNodeModulesPaths(args.path)
    for path in all_node_path:
        print(path)
    
    total_paths = len(all_node_path)

    confirm_rm = input("Are you sure you want to delete above "+str(total_paths)+" folder(y/n):").lower()
    if(confirm_rm == 'y'):
        for path in all_node_path:
            remove_directory(path)
        print("Removed "+str(total_paths)+' node_modules successfully!')
    return 1  
if __name__ == "__main__":
    main()
