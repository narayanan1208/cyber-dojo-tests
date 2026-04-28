import random


def init_doors(rng):
    doors = ["goat", "goat", "goat"]
    car_index = rng.randint(0, 2)
    doors[car_index] = "car"
    return doors


def player_choose(rng):
    return rng.randint(0, 2)


def host_open(doors, player_choice, rng):
    choices = [i for i in range(3) if i != player_choice and doors[i] == "goat"]
    return rng.choice(choices)


def switch_choice(player, opened):
    for i in range(3):
        if i != player and i != opened:
            return i


def stay_choice(player_choice):
    return player_choice


def is_win(doors, choice):
    return doors[choice] == "car"


def run_single_game(strategy, rng):
    doors = init_doors(rng)
    player_choice = player_choose(rng)
    opened = host_open(doors, player_choice, rng)

    if strategy == "switch":
        final_choice = switch_choice(player_choice, opened)
    elif strategy == "stay":
        final_choice = stay_choice(player_choice)
    else:
        raise ValueError("Invalid strategy")

    return is_win(doors, final_choice)


def simulate_games(strategy, n=1000, seed=None):
    rng = random.Random(seed)
    return sum(run_single_game(strategy, rng) for _ in range(n))


def compare_strategies(n=1000, seed=None):
    stay_wins = simulate_games("stay", n, seed)
    switch_wins = simulate_games("switch", n, seed)

    return {
        "stay": stay_wins,
        "switch": switch_wins,
        "stay_rate": stay_wins / n,
        "switch_rate": switch_wins / n,
    }
