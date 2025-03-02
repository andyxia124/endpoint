import sys
from classes import directory
         
def process_file_input(directory: directory.Directory, filename: str) -> None:
    """
    Processes a file and runs all the directory commands within the input file.

    Args:
        directory (str): Directory object defining current system scope.
        filename (str): Input file containing all directory commands to be run. 
    """
    with open(filename, 'r') as f:
        for line in f:
            if line:
                stripped = line.strip()
                print(stripped)
                words = stripped.split(' ')
                command = words[0].strip()

                #DEBUG
                #print(words)
                
                if command == 'CREATE':
                    if len(words) != 2:
                        print(f'Invalid number of arguments for command {command} 1 expected but {len(words) - 1} received')
                    else:
                        dir = words[1].strip()
                        directory.create(dir)
                elif command == 'MOVE':
                    if len(words) != 3:
                        print(f'Invalid number of arguments for command {command} 2 expected but {len(words) - 1} received')
                    else:
                        dir = words[1].strip()
                        destination = words[2].strip()
                        directory.move(dir, destination)
                elif command == 'DELETE':
                    if len(words) != 2:
                        print(f'Invalid number of arguments for command {command} 1 expected but {len(words) - 1} received')
                    else:
                        dir = words[1].strip()
                        directory.delete(dir)
                elif command == 'LIST':
                    if len(words) != 1:
                        print(f'Invalid number of arguments for command {command} 0 expected but {len(words) - 1} received')
                    else:
                        directory.list()
                else:
                    print(f'Invalid command entered: {command}')

                
def main(args):
    dir = directory.Directory()
    text_command = []

    for command in args:

        #Processing commands within a text file
        if '.txt' in command:
            process_file_input(dir, command)
        else:
            pass

if __name__ == '__main__':
    main(sys.argv[1:])