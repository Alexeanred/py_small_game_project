import random
#R: búa; P:báo; C: kéo
def play():
    player = input("R(búa) or P(bao) or C(kéo): ")
    AI = random.choice(['R','P','C'])
    if player == AI:
        return f'Hòa rồi do {player} = {AI}'
    else:
        if player=="R" and AI=="P":
            return f'Máy thắng do {player} < {AI}'
        elif player=="R" and AI=="C":
            return f'Máy thua do {player} > {AI}'
        elif player=="P" and AI=="C":
            return f'Máy thắng do {player} < {AI}'
        elif player=="P" and AI=="R":
            return f'Máy thua do {player} > {AI}'
        elif player=="C" and AI=="P":
            return f'Máy thua do {player} > {AI}'
        elif player=="C" and AI=="R":
            return f'Máy thắng do {player} < {AI}'
g = play()
print(g)
        