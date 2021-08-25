import random

def guess(x):
    feedback=''
    low = 1
    high = x
    while feedback != 'C':
        if low != high:
            guess = random.randint(low,high) #số máy tính đoán
        else:
            guess=low
        feedback =input(f"Có phải {guess} thấp(L) hoặc lớn(H) hoặc bằng(C)?") #feedback
        if feedback == "L":
            low = guess + 1
        elif feedback == "H":
            high= guess -1
    print(f'Máy đúng. Số đó là {guess}')
g = guess(20)

        
