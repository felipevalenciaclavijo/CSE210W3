import random


class Cards:
    """
   
    Attributes:
        
    """

    def __init__(self):
        """Constructs a new instance of Cards.

        Args:
            self (Cards): An instance of Cards.
        """
        self.value = random.randint(1, 13)

    def get_card(self):
        """Generates a new random value for the card.
        
        Args:
            self (Cards): An instance of Cards.
        """
        return self.value
       

        
