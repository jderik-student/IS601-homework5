# pylint: disable=unnecessary-dunder-call, invalid-name, unnecessary-pass

'''
    Defines the Application which is a REPL defined to be an interactive calculator
'''

from app.commands import CommandHandler
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand
from app.commands.getHistory import GetHistoryCommand
from app.commands.clearHistory import ClearHistoryCommand
from app.commands.menu import MenuCommand
from app.commands.exit import ExitCommand


class App:
    '''
        The Application is a REPL defined to be an interactive calculator
    '''
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()

    def start(self):
        '''
            Registers all the commands to be used by the user and starts the REPL
            Exits the app when the user types 'exit'
        '''
        # Register commands here
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("divide", DivideCommand())
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("getHistory", GetHistoryCommand())
        self.command_handler.register_command("clearHistory", ClearHistoryCommand())
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))

        self.command_handler.list_commands()
        print("Type 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Print, Loop
            self.command_handler.execute_command(input(">>> ").split())
