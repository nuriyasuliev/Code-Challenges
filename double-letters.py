def double_letters(text):
    for x in range(len(text)-1):
        if text[x] == text[x+1]:
         return True
    return False
print(double_letters('sweet'))
print(double_letters('bear'))