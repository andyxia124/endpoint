from typing import Optional, Dict

class Directory:
    """
    Represents a directory file system within a single system scope.

    Attributes:
        directories (Dict): Representation of diretory tree, a recursive mapping of parent directories to children directories.
    """
    def __init__(self) -> None:
        """
        Initializes the directory file system with root directory (Initially an empty map i.e. root has no parent).
        """
        self.directories = {}

    def create(self, dir: str) -> None:
        """
        Creates Directory within current system scope.

        Args:
            dir (str): Directory to be created.
        """
        if '/' in dir:
            path = dir.split('/')
            parent_dir_index = 0
            curr_dir = self.directories

            while parent_dir_index < len(path) - 1:
                parent_dir = path[parent_dir_index]
                if parent_dir not in curr_dir:
                    curr_dir[parent_dir] = {}
                curr_dir = curr_dir[parent_dir]
                parent_dir_index += 1

            new_dir = path[parent_dir_index]
            if new_dir in curr_dir:
                print(f'Directory {dir} already exists')
            else:
                curr_dir[new_dir] = {}

        else:
            if dir not in self.directories:
                self.directories[dir] = {}
            else:
                print(f'Directory {dir} already exists')


    def find_directory(self, dir: str) -> Optional[Dict]:
        """
        Helper function to assist in returning particular directory within current system scope, if it exists.

        Args:
            dir (str): Directory to search for.

        Returns:
            Optional[Dict]: Dictionary representing directory to be searched for if it exists, raise error if it does not exist

        """
        found_dir = self.directories
        child_dir = dir

        if '/' in dir:
            path = dir.split('/')
            parent_dir_index = 0

            while parent_dir_index < len(path) - 1:
                parent_dir = path[parent_dir_index]
                if parent_dir not in found_dir:
                    error_path = '/'.join(path[:parent_dir_index + 1])
                    raise Exception(error_path)
                found_dir = found_dir[parent_dir]
                parent_dir_index += 1
        
            child_dir = path[parent_dir_index]

        if child_dir not in found_dir:
            raise Exception(dir)
        
        return found_dir[child_dir]
        


    def move(self, dir: str, destination: str) -> None:
        """
        Moves directory to destination path within current system scope. Error log message printed if move is unable to be completed. 

        Args:
            dir (str): Directory to be moved.
            destination (str): New parent directory of the directory to be moved; directory to be moved will be placed within this directory.
        """
        try:
            moving_directory = self.find_directory(dir)
            self.delete(dir)

            new_dir = dir
            if '/' in dir:
                path = dir.split('/')
                new_dir = path[-1]
            
            new_parent_directory = self.find_directory(destination)
            new_parent_directory[new_dir] = moving_directory

        except Exception as e:
            print(e.args)
            print(f'Directory {dir} could not be moved to {destination} - {e.args[0]} does not exist')
        

    def delete(self, dir: str) -> None:
        """
        Delete the directory within current system scope. Error log message printed if directory does not exist.

        Args:
            dir (str): Directory to be deleted.
        """
        try:
            parent_directory = self.directories
            new_dir = dir

            if '/' in dir:
                path = dir.split('/')
                new_dir = path[-1]
                parent_path = '/'.join(path[:-1])
                parent_directory = self.find_directory(parent_path)
            
            parent_directory.pop(new_dir)
        except Exception as e:
            print(f'Cannot delete {dir} - {e.args[0]} does not exist')


    def list(self):
        """
        Print out all directories and subdirectories in hierarchical order, parent/children subdirectories indicated by preceding space indent. 

        """
        stack = []
        for parent_dir_name in sorted(self.directories.keys(), reverse=True):
            stack.append((parent_dir_name, self.find_directory(parent_dir_name), ''))

        while stack:
            dir_name, curr_dir, path = stack.pop()
            indent = path.count('/')
            if not path:
                path = dir_name + '/'
            print((' ' * indent) + dir_name)
             
            for child_dir_name in sorted(curr_dir.keys(), reverse=True):
                child_path = path + child_dir_name
                stack.append((child_dir_name, self.find_directory(child_path), child_path + '/'))
