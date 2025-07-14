letter = '''
        Dear <|Name|>,
        You are selected!
        <|Date|>
'''


print(letter.replace("<|Name|>","yash").replace("<|Date|>","1 july")) #after this string is as it is this is new string



print(letter) #after run above print but main string is as it is because ******strinng is immutable***************

#chaining replace