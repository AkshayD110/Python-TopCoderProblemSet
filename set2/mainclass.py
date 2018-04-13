from set2 import iterationScore

def main():
    word1 = input("Enter your first word")
    word2 = input("Enter your second word")
    word1 = word1.upper()
    word2 = word2.upper()
    if (len(word1) != len(word2)):
        raise ValueError("Both the words need to be of same lenght")


if __name__ == '__main__':
    main()
