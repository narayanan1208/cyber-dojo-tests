import string


def print_diamond_shape(alphabet: str):
    alphabets = string.ascii_uppercase
    alphabet_index = alphabets.index(alphabet)
    result = []

    for i in range(alphabet_index + 1):
        spaces = "." * (alphabet_index - i)
        if i == 0:
            result.append(f"{spaces}{alphabets[i]}{spaces}")
        else:
            inner_spaces = "." * (2 * i - 1)
            result.append(f"{spaces}{alphabets[i]}{inner_spaces}{alphabets[i]}{spaces}")

    for j in range(alphabet_index - 1, -1, -1):
        spaces = "." * (alphabet_index - j)
        if j == 0:
            result.append(f"{spaces}{alphabets[j]}{spaces}")
        else:
            inner_spaces = "." * (2 * j - 1)
            result.append(f"{spaces}{alphabets[j]}{inner_spaces}{alphabets[j]}{spaces}")

    return "\n".join(result)


if __name__ == "__main__":  # pragma: no cover
    print(print_diamond_shape("E"))
