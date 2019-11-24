import random
import logging


class LetsMakeADealGame:
    def __init__(self, switch: bool = False):
        self.switch = switch

        self.doors = [False, False, False]  # initialise all the doors to have no prize
        self.doors[random.randint(0, 2)] = True  # put the prize behind a random door
        logging.debug("We're ready to play!")

    def play(self) -> bool:
        random_doors = list(range(0, 3))
        random.shuffle(random_doors)

        chosen_door = random_doors[0]
        logging.debug("The Contestant has chosen door number %i", chosen_door + 1)

        if self.doors[random_doors[1]] is True:
            switch_door = random_doors[1]
            reveal_door = random_doors[2]
        else:
            switch_door = random_doors[2]
            reveal_door = random_doors[1]

        logging.debug("The host has revealed the prize is not behind door number %i", reveal_door + 1)

        if self.switch:
            logging.debug("The contestant has decided to switch to door number %i", switch_door + 1)
            final_choice = switch_door
        else:
            logging.debug("The contestant has decided to stick with door number %i", chosen_door + 1)
            final_choice = chosen_door

        if self.doors[final_choice] is True:
            logging.debug("Congratulations you're a winner!")
            return True
        else:
            logging.debug("Sorry, you're going home with nothing.")
            return False

