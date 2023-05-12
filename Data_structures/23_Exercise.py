from collections import Counter

# convert python string to list function is defined here


def Convert(string):
    list1 = []
    list1[:0] = string
    return list1


# given sentence is mentioned here
sentence = "This is comman interview quection"

# convert all characters to the lowercase
sentence = sentence.lower()

# call the conver funnction and convert sring to list
sentence = (Convert(sentence))

# its prints converted list
print(sentence)

# the counter converts list to dictionary
# using we can get count of keys like " keys : value"
new = (Counter(sentence))
print(new)

# then we can sort value with any number of arguments using lambda function.
# its display sorted value of every keys
sorted = sorted(new.items(), key=lambda item: item[1])
print(sorted)

# using these expression we can get the last key and value of dictionary.
#last_key = list(sorted)[-1]
print(sorted[-1])
