#!/usr/bin/python3
"""
The entry point of the command interpreter
"""
import cmd


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
