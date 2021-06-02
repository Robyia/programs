"""5: Write a Python program that takes a text file as input and returns the number of
words of a given text file."""

fname=input("enter fil name:")
wordcount=0
with open(fname,'r')as f:
    for line in f:
        words=line.split()
        wordcount+=len(words)

print("number of words:")
print(wordcount)
        

