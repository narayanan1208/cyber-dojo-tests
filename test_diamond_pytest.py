from diamond import print_diamond_shape


def test_print_diamond_shape_A():
    expected = "A"
    assert print_diamond_shape("A") == expected


def test_print_diamond_shape_B():
    expected = "\n".join([".A.", "B.B", ".A."])

    assert print_diamond_shape("B") == expected


def test_print_diamond_shape_C():
    expected = "\n".join(["..A..", ".B.B.", "C...C", ".B.B.", "..A.."])
    assert print_diamond_shape("C") == expected


def test_print_diamond_shape_D():
    expected = "\n".join(
        ["...A...", "..B.B..", ".C...C.", "D.....D", ".C...C.", "..B.B..", "...A..."]
    )
    assert print_diamond_shape("D") == expected


def test_print_diamond_shape_E():
    expected = "\n".join(
        [
            "....A....",
            "...B.B...",
            "..C...C..",
            ".D.....D.",
            "E.......E",
            ".D.....D.",
            "..C...C..",
            "...B.B...",
            "....A....",
        ]
    )
    assert print_diamond_shape("E") == expected
