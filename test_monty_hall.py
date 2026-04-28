import random

from monty_hall import (
    host_open,
    init_doors,
    is_win,
    player_choose,
    run_single_game,
    simulate_games,
    stay_choice,
    switch_choice,
)


def test_init_doors_has_one_car():
    doors = init_doors(random.Random(45))
    assert doors.count("car") == 1


def test_player_choice_valid():
    choice = player_choose(random.Random(45))
    assert choice in [0, 1, 2]


def test_host_not_player_choice():
    doors = ["car", "goat", "goat"]
    opened = host_open(doors, player_choice=0, rng=random.Random(42))
    assert opened != 0


def test_host_opens_goat():
    doors = ["car", "goat", "goat"]
    opened = host_open(doors, player_choice=0, rng=random.Random(42))

    assert doors[opened] == "goat"


def test_switch_changes_choice():
    assert switch_choice(0, 1) == 2


def test_stay_choice():
    assert stay_choice(2) == 2


def test_is_win():
    doors = ["car", "goat", "goat"]
    assert is_win(doors, 0)


def test_run_single_game_returns_bool():
    result = run_single_game("stay", random.Random(1))
    assert isinstance(result, bool)


def test_probability_stay():
    wins = simulate_games("stay", n=10000, seed=42)
    rate = wins / 10000
    assert 0.28 < rate < 0.38


def test_probability_switch():
    wins = simulate_games("switch", n=10000, seed=42)
    rate = wins / 10000
    assert 0.60 < rate < 0.72


def test_switch_better():
    stay = simulate_games("stay", 3, seed=42)
    switch = simulate_games("switch", 3, seed=42)
    assert switch > stay
