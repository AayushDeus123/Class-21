#Matching words
def match_word(words):
    lst = []
    ctr = 0
    
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr +=1
            lst.append(word)
        
    print('List of words with first character and last character same \n:',lst)
    return ctr
a = ['abc','aba','121','123','xyz','19321']
print(match_word(a))