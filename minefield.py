def generate_hint_field(n: int, m: int, field: list) -> list:
    result = []

    for i in range(n):
        row = ""
        for j in range(m):
            if field[i][j] == "*":
                row += "*"
            else:
                count = 0

                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue

                        ni, nj = i + dx, j + dy

                        if 0 <= ni < n and 0 <= nj < m:
                            if field[ni][nj] == "*":
                                count += 1
                row += str(count)
        result.append(row)
    return result


def print_hint_field(result) -> str:
    return "\n".join(result)


if __name__ == "__main__":  # pragma: no cover
    n, m = 3, 4

    field = ["*...", "..*.", "...."]
    print(print_hint_field(generate_hint_field(n, m, field)))
