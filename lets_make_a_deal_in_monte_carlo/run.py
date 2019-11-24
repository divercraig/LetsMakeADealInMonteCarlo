import logging
from lets_make_a_deal_in_monte_carlo.lets_make_a_deal import LetsMakeADealGame

logging.basicConfig(format='%(message)s', level=logging.INFO)


def run_a_game(game_number: int, switch: bool):
    win = False
    game = LetsMakeADealGame(switch=switch)
    if game.play() is True:
        logging.debug("Game %i was a winner", game_number)
        win = True
    else:
        logging.debug("Game %i was a loser", game_number)
    logging.debug("+++++++++++++++++++++++++++++")
    return win


def run_a_simulation(num_games: int, switch: bool):
    wins = 0
    strategy_name = "SWITCH" if switch is True else "STICK"
    logging.info("RUNNING %i GAMES WITH THE %s STRATEGY", num_games, strategy_name)
    for x in range(1, num_games + 1):
        if run_a_game(switch=switch, game_number=x) is True:
            wins += 1

    logging.info("COMPLETED %i GAMES WITH THE %s STRATEGY- %i WON", num_games, strategy_name, wins)
    logging.info("-----------------------------------------------")

    return wins / num_games * 100


sample_size = 100000

stick_success_rate = run_a_simulation(num_games=sample_size, switch=False)
switch_success_rate = run_a_simulation(num_games=sample_size, switch=True)

logging.info("SIMULATIONS COMPLETE")
logging.info("Stick won %d percent of the time", stick_success_rate)
logging.info("Switch won %d percent of the time", switch_success_rate)



