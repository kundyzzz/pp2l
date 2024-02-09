def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence

user_input = input("Enter a sentence: ")
reversed_sentence = reverse_words(user_input)
print("Reversed sentence:", reversed_sentence)