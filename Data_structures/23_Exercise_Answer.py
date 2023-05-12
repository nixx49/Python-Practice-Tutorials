from pprint import pprint
# pprint use for print the dictionaries

sentence = "This is a comman interview quection"
# define a dictionary as char_frequency

char_frequency = {}

# for loop for get the character count
# for filter characters in sentence
for char in sentence:
    # for filter character frequency
    if char in char_frequency:
        # if character in many times, itwork as "char = char + 1"
        char_frequency[char] += 1
    else:
        # if no frequency its stable
        char_frequency[char] = 1

sorted = sorted(char_frequency.items(),
                key=lambda item: item[1],
                reverse=True)

print(sorted[0])
