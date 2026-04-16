import pytest

from minefield import generate_hint_field, print_hint_field


def test_minefield_input_success():
    field = ["*...", "..*.", "...."]
    assert generate_hint_field(3, 4, field) != []


def test_minefield_input_failure():
    field = ["*...", "..*.", "...."]
    with pytest.raises(TypeError):
        assert generate_hint_field("3", 4, field) != []


def test_minefield_field_input():
    field = []
    with pytest.raises(TypeError):
        assert generate_hint_field("3", 4, field) == []


def test_mine_hint_field_case1():
    field = ["*...", "..*.", "...."]
    assert generate_hint_field(3, 4, field) == ["*211", "12*1", "0111"]


def test_mine_hint_field_case2():
    field = ["...", ".*.", "..."]
    assert generate_hint_field(3, 3, field) == ["111", "1*1", "111"]


@pytest.mark.parametrize(
    "field, expected_output",
    [
        (["...", ".*.", "..."], "111\n1*1\n111"),
        (["*..", "...", "..."], "*10\n110\n000"),
    ],
)
def test_print_hint_field(field, expected_output):
    n = len(field)
    m = len(field[0])

    result = generate_hint_field(n, m, field)

    assert print_hint_field(result) == expected_output
