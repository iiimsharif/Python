def count_vowels(text):
    vowels = ["a", "o", "e", "i", "u", "A", "O", "E", "I", "U"]
    count = 0
    for i in range(len(text)):
        if text[i] in vowels:
            count += 1
    return count


user_input = input("Write a string:\n")
count_answer = count_vowels(user_input)
print(f"\nthere are {count_answer} vowels in \n{user_input}")
