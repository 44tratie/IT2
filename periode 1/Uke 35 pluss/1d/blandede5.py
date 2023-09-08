import random

board = [["" for _ in range(3)] for _ in range(3)]  # lager et 3*3 brett

Coordinate = tuple[int, int]

print(
    "Brettet fungerer som et sjakkbrett, ruten nedre til venstre er A1 og ruten på toppen til høyre er C3."
)

player_turn = "x"
vs_machine = None
while vs_machine is None:
    try:
        vs_machine_prompt = input("Vil du spille singleplayer? (ja/nei): ").lower()
        assert vs_machine_prompt in {"ja", "nei"}
        vs_machine = True if vs_machine_prompt == "ja" else False
    except AssertionError:
        print("ugyldig svar")


def board_no_space() -> bool:
    for row in board:
        if not all(row):
            return False
    return True


def player_won() -> bool:
    for row in range(3):
        first = board[row][0]
        if not first:
            continue
        if all(board[row][col] == first for col in range(1, 3)):
            return True
    for col in range(3):
        first = board[0][col]
        if not first:
            continue
        if all(board[row][col] == first for row in range(1, 3)):
            return True
    first = board[0][0]
    if first:
        if all(board[i][i] == first for i in range(1, 3)):
            return True
    first = board[0][2]
    if first:
        if all(board[i][3 - i] == first for i in range(1, 3)):
            return True
    return False


def ask_for_coordinate() -> Coordinate:
    while True:
        try:
            coordinate = input("skriv koordinat: ").lower()
            if (col := coordinate[0]) not in "abc":
                raise ValueError
            if not 1 <= (row := int(coordinate[-1])) <= 3:
                raise ValueError
            col = ord(col) - 97
            row = 3 - row
            return row, col
        except ValueError:
            print("ugyldig koordinat")


def get_coordinate() -> Coordinate:
    while True:
        try:
            coordinate: Coordinate = ask_for_coordinate()
            if board[coordinate[0]][coordinate[1]]:
                raise ValueError
            return coordinate
        except ValueError:
            print("feltet er allerede tatt!")


def flip_player_turn():
    global player_turn
    player_turn = "o" if player_turn == "x" else "x"


def print_board():
    for row in board:
        print(
            "|".join((f"{row[col]:^5}" for col in range(len(row)))),
            end="\n-----------------\n",
        )


while True:
    if player_won():
        print_board()
        flip_player_turn()
        print(f"{player_turn} spilleren vant!")
        exit()
    if board_no_space():
        print_board()
        print("uavgjort!")
        exit()

    if vs_machine and player_turn == "o":
        fields = [(row, col) for row in range(3) for col in range(3)]
        random.shuffle(fields)
        for row, col in fields:
            if board[row][col]:
                continue
            board[row][col] = "o"
            break
    else:
        print(f"det er {player_turn} sin tur!")
        print_board()
        row, col = get_coordinate()
        board[row][col] = player_turn
    flip_player_turn()
