def words(word):
    if len(word) > 10:
        return word.upper()
    else:
        return word
    
print(words("hello world"))
print(words("goodbye"))