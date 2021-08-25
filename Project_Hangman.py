import random
import string
from words import words
def get_valid_word(words):
    word = random.choice(words) #chọn 1 từ ngẫu nhiên từ list words
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()
def hangman():
    word= get_valid_word(words)
    word_letters = set(word) #những chữ cái trong từ đó
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #chữ đã doán
    lives = 8
    while len(word_letters) > 0 and lives >0:
        #Các từ đã sử dụng
        print('Bạn còn ', lives ,'mạng nũa và các từ bạn đã dùng: ', ' '.join(used_letters)) 
        #Các từ đã đoán gần đây
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Các từ gần đây: ', ' '.join(word_list))
        #Users nhập từ
        user_letter = input("Nhập chữ cái: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives -1 #nếu sai trừ 1 mạng
                print('Chữ đó ko có trong từ.')
        elif user_letter in used_letters:
            print('Bạn đoán từ đó rồi nha. Thử từ khác đi!!!')
        else:
            print('Từ không hợp lệ. Đoán lại!!!')
    #khi bạn đoán đúng hết hoặc bạn đã hết mạng
    if lives==0:
        print('Bạn đã thua. Từ cần đoán là: ', word, '.Chúc may mắn lần sau.')
    else:
        print('Bạn đã đoán đúng rồi. Nếu can đảm hãy chơi lại.')

g= hangman()
