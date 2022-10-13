import chess
import chess.pgn
import random
import base64

#board = chess.Board()

leet_replacements = {
    'a': ['a', 'A', '@', '4'],
    'b': ['b', 'B', '8'],
    'c': ['c', 'C'],
    'd': ['d', 'D'],
    'e': ['e', 'E', '3'],
    'f': ['f', 'F'],
    'g': ['g', 'G', '6'],
    'h': ['h', 'H', '#'],
    'i': ['i', 'I', '1', '!', '|'],
    'j': ['j', 'J'],
    'k': ['k', 'K'],
    'l': ['l', 'L', '1', '|'],
    'm': ['m', 'M'],
    'n': ['n', 'N'],
    'o': ['o', 'O', '0'],
    'p': ['p', 'P'],
    'q': ['q', 'Q'],
    'r': ['r', 'R'],
    's': ['s', 'S', '5', '$', 'z', 'Z'],
    't': ['t', 'T', '7'],
    'u': ['u', 'U'],
    'v': ['v', 'V'],
    'w': ['w', 'W'],
    'x': ['x', 'X'],
    'y': ['y', 'Y'],
    'z': ['z', 'Z', 's', 'S', '5', '$'],
    '_': ['_', ' ', '-'],
    ' ': ['_', ' ', '-', '.'],
    '*': ['*', 'x', 'X', '%'],
    '!': ['!', '1', '|'],
    '(': ['(', '[', '{'],
    ')': [')', ']', '}'],
    '0': ['0', 'O', 'o'],
    '"': ['"', "'", '`'],
}

def get_leet(char):
    char = char.lower()
    if char in leet_replacements:
        return leet_replacements[char]
    else:
        return [char]

def convert_random_leet(phrase):
    new_phrase = ""
    for letter in phrase:
        if letter.lower() in leet_replacements:
            new_phrase += random.choice(leet_replacements[letter.lower()])
        else:
            new_phrase += letter
    return new_phrase

def dfs2(board, moves, depth, coord_list):
    if depth == len(coord_list):
        return moves
    for move in board.legal_moves:
        if move.to_square == coord_list[depth]:
            board.push(move)
            moves.append(move)
            result = dfs2(board, moves, depth + 1, coord_list)
            if result:
                return result
            board.pop()
            moves.pop()

base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
def get_coords(phrase):
    encoded = base64.b64encode(phrase.encode('utf-8'))
    coords = []
    for char in encoded:
        if chr(char) == '=':
            continue
        coords.append(base64_chars.index(chr(char)))
    return coords

def apply_to_board(board, coord_list):
    moves = dfs2(board, [], 0, coord_list)
    if moves is None:
        return 0
    for move in moves:
        board.push(move)
    return len(moves)

# make sure target is divisible by 3
#all = "Are you kidding ??? What the **** are you talking about man ? You are a biggest looser i ever seen in my life ! You was doing PIPI in your pampers when i was beating players much more stronger then you! You are not proffesional, because proffesionals knew how to lose and congratulate opponents, you are like a girl crying after i beat you! Be brave, be honest to yourself and stop this trush talkings! Everybody know that i am very good blitz player, i can win anyone in the world in single game! And \"w\"esley \"s\"o is nobody for me, just a player who are crying every single time when loosing, ( remember what you say about Firouzja ) ! Stop playing with my name, i deserve to have a good name during whole my chess carrier, I am Officially inviting you to OTB blitz match with the Prize fund! Both of us will invest 5000$ and winner takes it all! I suggest all other people who's intrested in this situation, just take a look at my results in Blitz World championships, and that should be enough. No need to listen for every crying babe, Tigran Petrosyan is always play Fair ! And if someone will continue Officially talk about me like that, we will meet in Court! God bless with true! True will never die ! Liers will kicked off"
all = "whatif hans cheated by bringing in extra chess pieces in his pockets and placed them on the board when noone was looking?"
# pad with '!'
all = all + "!" * (3 - len(all) % 3)
assert len(all) % 3 == 0
goal = get_coords(all)

# We bruteforce characters in the phrase, but since the phrase gets encoded to base64
# we need to bruteforce characters one at a time but in pairs
# This is because base64 is 6 bits per character, so we need to bruteforce 2 characters
def bruteforce2(board, phrase, depth, all_moves):
    if depth >= len(all):
        print("Found phrase: " + phrase)
        return phrase
    chars = all[depth:depth+3]
    choices1 = get_leet(chars[0])
    choices2 = get_leet(chars[1])
    choices3 = get_leet(chars[2])
    # cartesian product
    choices = [c1 + c2 + c3 for c1 in choices1 for c2 in choices2 for c3 in choices3]
    random.shuffle(choices)
    for possible_groups in choices:
        new_phrase = phrase + possible_groups
        print(new_phrase)
        moves = dfs2(board, [], 0, get_coords(possible_groups))
        if moves is None:
            continue
        print(new_phrase)
        all_moves.extend(moves)
        result = bruteforce2(board, new_phrase, depth + 3, all_moves)
        if result:
            return all_moves
        for move in moves:
            board.pop()
            all_moves.pop()
    return None

#board_pgn = "q1Q1q1Q1/7q/Q7/7Q/q7/7q/Q7/1q1Q1q1Q w KQkq - 0 1"
board_pgn = "rnbqkbnr/8/8/8/8/8/8/RNBQKBNR w KQkq - 0 1"

moves = bruteforce2(chess.Board(board_pgn), "", 0, [])
print(moves)

# save to pgn
game = chess.pgn.Game()
game.setup(chess.Board(board_pgn))
node = game.add_variation(moves[0])
for move in moves[1:]:
    node = node.add_variation(move)
with open("moves_wow.pgn", "w") as f:
    f.write(str(game))
        
