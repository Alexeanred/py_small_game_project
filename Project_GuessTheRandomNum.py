import random

def guess_the_num(x):
    random_number = random.randint(1, x)
    input_ =0 #cho input=0 để ko bị lỗi khai báo và ko trùng với số random
    while input_ != random_number:
        input_ = int(input(f"Guess the number between 1 and {x}: "))
        if input_ > random_number:
            print('Quá cao nha')
        elif input_ < random_number:
            print('Quá thấp nha')
    print('You are right')
g= guess_the_num(20)
print(g)