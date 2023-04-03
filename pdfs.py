n = int(input())
lst = list(map(int, input().split()))
odd = [i for i in lst if i % 2 != 0]
even = [i for i in lst if i % 2 == 0]
if len(odd) > len(even):
    print("NO")
else:
    print("YES")
print(*odd)
print(*even)


def create_matrix():
    matrix = []
    for i in range(3):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

matrix = create_matrix()
diag_sum = sum(matrix[i][i] for i in range(3))
print("Diagonals :", diag_sum)




def create_cv():
    name = input("Введите ФИО: ")
    age = input("Введите возраст: ")
    email = input("Введите электронную почту: ")
    phone = input("Введите номер телефона: ")
    skills = input("Введите навыки через запятую: ")
    experience = input("Введите опыт работы: ")
    education = input("Введите образование: ")
    cv = {
        "ФИО": name,
        "Возраст": age,
        "Электронная почта": email,
        "Номер телефона": phone,
        "Навыки": skills.split(","),
        "Опыт работы": experience,
        "Образование": education
    }
    return cv

cv = create_cv()
print(cv)



def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    elif n <= 0:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    n = 10
    for i in range(1, n + 1):
        print("fibonacci number", i, "=", fibonacci(i))


def is_power_of_two(n):
    if n <= 0:
        return False
    else:
        return (n & (n-1)) == 0


def print_board(board):
    print("-------------")
    for i in range(3):
        row = "|"
        for j in range(3):
            row += " " + str(board[i*3+j]) + " |"
        print(row)
        print("-------------")

def get_move(player, board):
    while True:
        move = input("Куда поставим " + player + "? ")
        if move.isdigit() and int(move) >= 1 and int(move) <= 9 and board[int(move)-1] == " ":
            return int(move) - 1
        else:
            print("Некорректный ход. Попробуйте еще раз.")

def check_win(board):
    for i in range(3):
        if board[i*3] == board[i*3+1] == board[i*3+2] != " ":
            return board[i*3]
        if board[i] == board[i+3] == board[i+6] != " ":
            return board[i]
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]
    if " " not in board:
        return "Ничья"
    return None

def tic_tac_toe():
    print("********** Игра Крестики-нолики для двух игроков **********")
    board = [" "]*9
    print_board(board)
    player = "X"
    while True:
        move = get_move(player, board)
        board[move] = player
        print_board(board)
        winner = check_win(board)
        if winner:
            print(winner + " выиграл!")
            break
        player = "O" if player == "X" else "X"

tic_tac_toe()