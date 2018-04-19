from set2 import iterationScore

def main():
    word1 = input("Enter your first word")
    word2 = input("Enter your second word")
    word1 = word1.upper()
    word2 = word2.upper()
    #below two conditions check the input condition
    assert len(word1)==len(word2), "Both the words should be of same length"
    #if (len(word1) != len(word2)):
     #   raise ValueError("Both the words need to be of same lenght")
    if (len(word1) and len(word2) > 50):
        raise ValueError(f"Length of {word1} and {word2} should be less than 50 characters")
    get_score_obj = iterationScore.iterationScore(word1, word2)
    get_score_obj.score_calculator()

if __name__ == '__main__':
    main()
