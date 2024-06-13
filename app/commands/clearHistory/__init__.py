# pylint: disable=unnecessary-dunder-call, invalid-name
'''
    Defines the REPL command to delete the Calculator's History
'''

from decimal import Decimal
from typing import List
from app.commands import Command
from app.calculator import CalculatorHistory

class ClearHistoryCommand(Command):
    """
        This class extends the Abstract Command Class and deletes all calcualtions from the Calculator's History
    """

    def execute(self, user_input: List[Decimal]):
        """
            Deletes all calculations from the Calculator's history

            @param user_input: not used by this method, added to adhere to Liskov substitution principle
        """
        try:
            CalculatorHistory.delete_history()
        except Exception as e: # Catch-all for unexpected errors
            print(f"An error occurred: {e}")
