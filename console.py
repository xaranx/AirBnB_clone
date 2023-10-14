#!/usr/bin/python3
"""
The entry point of the command interpreter
"""
import cmd
from models.engine.file_storage import FileStorage
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import sys
import json


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class
    """
    prompt = '(hbnb) '

    classes = [
            'BaseModel',
            'User',
            'State',
            'City',
            'Amenity',
            'Place',
            'Review'
            ]

    commands = [
            'create()',
            'all()',
            'count()'
            ]

    commands_with_id = [
            'show',
            'destroy'
            ]

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

        elif len(args) >= 1:
            for class_ in HBNBCommand.classes:
                if args[0] == class_:
                    new_instance = globals()[class_]()
                    new_instance.save()
                    print(f'{new_instance.id}')

        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the
        class name and id
        """
        args = line.split()

        if len(args) >= 2:
            if args[0] not in HBNBCommand.classes:
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
            if args[0] not in HBNBCommand.classes:
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
        instances = []
        if len(args) == 0:
            for instance in available_instances:
                instances.append(str(available_instances[instance]))
            print(instances)

        else:
            if args[0] in HBNBCommand.classes:
                for instance in available_instances:
                    if args[0] in instance:
                        instances.append(str(available_instances[instance]))
                print(instances)
            else:
                print('** class doesn\'t exist **')
                return

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        """
        args = line.split()
        args = list(map(lambda x: x.strip('"'), args))

        available_instances = storage.all()
        if len(args) >= 4:
            if args[0] not in HBNBCommand.classes:
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

    def do_count(self, line):
        """
        Countes how many instances of a class
        The same method used for do_all except return values
        Returns the length
        """
        args = line.split()

        available_instances = storage.all()
        instances = []
        if len(args) == 0:
            for instance in available_instances:
                instances.append(str(available_instances[instance]))
            print(len(instances))

        else:
            if args[0] in HBNBCommand.classes:
                for instance in available_instances:
                    if args[0] in instance:
                        instances.append(str(available_instances[instance]))
                print(len(instances))
            else:
                print('** class doesn\'t exist **')
                return

    def precmd(self, line):
        """
        Accessing the command before onecmd
        """
        args = line.split('.')

        if len(args) >= 2:
            for class_ in HBNBCommand.classes:
                if args[0] == class_:
                    if args[1] in HBNBCommand.commands:
                        for command in HBNBCommand.commands:
                            if args[1] == command:
                                return f"{args[1][:-2]} {args[0]}"
                else:
                    cmd = args[1].split('(')
                    if cmd[0] == 'update':
                        params = cmd[1].split(', ')
                        prms = list(map(lambda x: x.strip('")'), params))
                        return "{} {} {} {} {}"\
                            .format(cmd[0], args[0], prms[0], prms[1], prms[2])
                    elif cmd[0] in HBNBCommand.commands_with_id:
                        for command in HBNBCommand.commands_with_id:
                            if cmd[0] == command:
                                return f"{cmd[0]} {args[0]} {cmd[1][1:-2]}"
        return line

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
