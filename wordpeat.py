text = input("Enter a sentence: ")

words = text.split()  

for word in set(words):  
    count = words.count(word)
    print(f"The word '{word}' repeats {count} times.")
