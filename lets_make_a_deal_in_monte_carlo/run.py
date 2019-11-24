import logging
from lets_make_a_deal_in_monte_carlo.lets_make_a_deal import LetsMakeADealGame

logging.basicConfig(format='%(message)s', level=logging.INFO)
sample_size = 100000
stick_wins = 0
switch_wins = 0

logging.info("RUNNING %i STICK SIMULATIONS", sample_size)
for x in range(1, sample_size + 1):
    game = LetsMakeADealGame()
    if game.play() is True:
        logging.debug("Game %i was a winner", x)
        stick_wins += 1
    else:
        logging.debug("Game %i was a loser", x)
    logging.debug("+++++++++++++++++++++++++++++")

logging.info("COMPLETED %i STICK SIMULATIONS - %i WON", sample_size, stick_wins)

logging.info("-----------------------------------------------")

logging.info("RUNNING %i SWITCH SIMULATIONS", sample_size)
for x in range(1, sample_size + 1):
    game = LetsMakeADealGame(switch=True)
    if game.play() is True:
        logging.debug("Game %i was a winner", x)
        switch_wins += 1
    else:
        logging.debug("Game %i was a loser", x)
    logging.debug("+++++++++++++++++++++++++++++")

logging.info("COMPLETED %i SWITCH SIMULATIONS - %i WON", sample_size, switch_wins)

logging.info("-----------------------------------------------")

logging.info("SIMULATIONS COMPLETE")
logging.info("Stick won %d percent of the time", stick_wins/sample_size * 100)
logging.info("Switch won %d percent of the time", switch_wins/sample_size * 100)
