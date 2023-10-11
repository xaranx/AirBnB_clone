#!/usr/bin/python3
"""
The entry point of the command interpreter
"""
import cmd
from models.engine.file_storage import FileStorage
from models.__init__ import storage
from models.base_model import BaseModel
import sys


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class
    """
    prompt = '(hbnb) '

    def onecmd(self, line):
        """
        Ignores empty lines
        """
        if not line.strip():
            return
        return super().onecmd(line)

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it to the JSON file
        and prints the id
        """
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")

        elif args[0] in globals():
            new_instance = globals()[args[0]]()
            new_instance.save()
            print(f'{new_instance.__dict__["id"]}')

        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the
        class name and id
        """
        args = line.split()

        if len(args) >= 2:
            if not args[0][0].isupper():
                print('** class name is missing **')
            
            elif args[0] != 'BaseModel':
                print('** class doesn\'t exist **')

            else:
                look_up = '{}.{}'.format(args[0], args[1])
                with open(FileStorage.__file_path, 'r') as f:
                    if look_up in f.keys():
                        data = json.load(f[look_up])
                print('[{}] ({}) {}'.format(args[0], args[1], data))

        elif len(args) == 1:
            print('** instance id missing **')

        else:
            print('** class name is missing **')

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        args = line.split()

        if len(args) >= 2:
            if not args[0][0].isupper():
                print('** class name missing **')
            
            elif args[0] != 'BaseModel':
                print('** class doesn\'t exist **')

            else:
                look_up = '{}.{}'.format(args[0], args[1])
                with open(FileStorage.__file_path, 'r') as f:
                    if look_up in f.keys():
                        del f[look_up]
                        storage.save()

        elif len(args) == 1:
            print('** instance id missing **')

        else:
            print('** class name missing **')


    def do_all(self, line):
        """
        Prints all string representation of all instances based or
        not on the class name.
        """

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        """

    def do_EOF(self, line):
        """
        Exits the program
        """
        return True

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
