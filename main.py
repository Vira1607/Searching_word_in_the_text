def search(t, w):
    a = "Word not found"
    text = t.split(' ')
    for i in text:
        if word == i:
            a = "Word found"
    return a


text = input('')
word = input('')

print(search(text, word))