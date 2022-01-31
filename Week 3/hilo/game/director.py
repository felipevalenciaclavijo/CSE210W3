from game.cards import Cards


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.cards = [Cards().value]
        self.is_playing = True
        self.points = 300
        self.hilo_guess = ""

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            self.play_again()
        print(f"Your final score is {self.points}")
        print("Thank You for playing!")


    def play_again(self):
        """Ask the user if they want to  play again?

        Args:
            self (Director): An instance of Director.    
        """
        keep_playing = input("Play again? [y/n] ")
        self.is_playing = (keep_playing == "y")
    
    

    def get_inputs(self):
        """Ask the user if they want to draw a card.

        Args:
            self (Director): An instance of Director.
        """

        new_card = Cards()
        self.cards.append(new_card.get_card())
        print()
        print(f"The card is: {self.cards[-2]}")
        

        self.hilo_guess = input("Higher or lower? [h/l] ").lower()
        
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        
        if not self.is_playing:
            return 
        
        if self.hilo_guess == "h":
            if self.cards[-2] <= self.cards[-1]:
                self.points += 100
            else:
                self.points -= 75
        elif self.hilo_guess == "l":
            if self.cards[-2] >= self.cards[-1]:
                self.points += 100
            else:
                self.points -= 75

        self.is_playing == (self.points > 0)
            
            
    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        print(f"Next card was: {self.cards[-1]}")
        print(f"Your score is: {self.points}")
        self.is_playing == (self.points > 0)