# list
letters = ["a", "b", "c","d","e","f","t","y","r"]
matrix = [[0,1], [2,3]]
zeros = [0] * 5
combined = zeros + letters
print(combined)
numbers = list(range(20))
char = list("hello world")
print(numbers)
print(char)
# Accessing Items
print(letters[0])
print(letters[-1])
print(letters[0:1])
print(letters[0:])
print(numbers[::2])
print(numbers[::-1])
# unpacking list
number = [1, 2, 3, 4, 5, 6]
first, second, *other = number
print(first)
print(second)
print(other)
# looping over lists
for index, letter in enumerate(letters):
    print(letter)
    print(index, letter)
# add and remove item 
# add
letters.append("e")
letters.insert(2,"E")
# remove
letters.pop(0)
letters.remove("b")
del letters[0:2]
print(letters)
# finding item
print(letters.index("f"))
# sort list
print(sorted(numbers,reverse=True))
print(numbers)
items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
    ("product4", 14),
]
def sort_items(items):
    return items[1]
items.sort(key=sort_items)
print(items)
#Map Function 