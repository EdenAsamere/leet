import string
def pangram(sentence):
    res = [*set(sentence)]
    res.sort()
    res = ''.join(res)
    if res == string.ascii_lowercase:
        print(True)
    print(res)
    print(string.ascii_lowercase)

sentence = "thequickbrownfoxjumpsoverthelazydog"
pangram(sentence)
