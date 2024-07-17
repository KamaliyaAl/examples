def count_char_frequency(sentence):
    char_frequency = list()
    for char in sentence:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    return char_frequency


print(count_char_frequency("Hello, World!"))
#AI understands the context