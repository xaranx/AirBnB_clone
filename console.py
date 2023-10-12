#!/usr/bin/python3
"""
The entry point of the command interpreter
"""
import cmd
from models.engine.file_storage import FileStorage
from models.__init__ import storage
from models.base_model import BaseModel
import sys
import json


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
            if args[0] != 'BaseModel':
                print('** class name doesn\'t exist **')
                return

            else:
                look_up = '{}.{}'.format(args[0], args[1])
                available_instances = storage.all()
                if look_up in available_instances.keys():
                    print(available_instances[look_up])
                    return

                else:
                    print("** no instance found **")
                    return

        elif len(args) == 1:
            if not args[0][0].isupper():
                print('** class name missing **')
                return

            else:
                print("** instance id missing **")
                return
        else:
            print('** class name missing **')
            return

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        args = line.split()

        if len(args) >= 2:
            if args[0] != 'BaseModel':
                print('** class name doesn\'t exist **')
                return

            else:
                look_up = '{}.{}'.format(args[0], args[1])
                available_instances = storage.all()
                
                if look_up in available_instances:
                    del available_instances[look_up]
                    storage.save()
                
                else:
                    print("** no instance found **")
                    return

        elif len(args) == 1:
            if not args[0][0].isupper():
                print('** class name missing **')
                return

            else:
                print("** instance id missing **")
                return
        else:
            print('** class name missing **')
            return

    def do_all(self, line):
        """
        Prints all string representation of all instances based or
        not on the class name.
        """
        args = line.split()

        available_instances = storage.all()
        list_of_instances = []
        if len(args) == 0:
            for instance in available_instances:
                list_of_instances.append(str(available_instances[instance]))
            print(list_of_instances)

        else:
            if args[0] == 'BaseModel':
                for instance in available_instances:
                    if args[0] in instance:
                        list_of_instances.append(str(available_instances[instance]))
                print(list_of_instances)
            else:
                print('** class doesn\'t exist **')
                return

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        """
        args = line.split()

        available_instances = storage.all()
        if len(args) >= 4:
            if args[0] != 'BaseModel':
                print("** class doesn't exist **")
                return

            key = '{}.{}'.format(args[0], args[1])
            if key in available_instances.keys():
                setattr(available_instances[key], args[2], args[3])
                storage.save()

            else:
                print("** no instance found **")
                return

        elif len(args) == 3:
            print("** value missing **")
            return

        elif len(args) == 2:
            print("** attribute name is missing **")
            return

        elif len(args) == 1:
            print("** instance id missing **")
            return

        else:
            print("** class name missing **")
            return

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
