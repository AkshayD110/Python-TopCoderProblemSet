from collections import Counter

def score_calculation(word):
    '''Below two conditions to check inputs validations'''
    if (len(word)>50):
        raise ValueError("The length of input word should be with in 50characters")
    #Below 2 lines to check the input word contains smallcase character
    if not (word.isupper()):
        raise ValueError("The word should be in upper case")
    #below section for replacing second most occuring char with first
    word_cntr=Counter(list(word))
    two_common_characters=word_cntr.most_common(2)
    first_common=two_common_characters[0]
    first_char=first_common[0]
    second_common=two_common_characters[1]
    second_char=second_common[0]

    #below section for score calculation
    word=word.replace(second_char, first_char)
    word_cntr = Counter(list(word))
    print(word_cntr)
    score_list=list(word_cntr.values())
    total_score=sum([(x*x) for x in score_list]) #list comprehension to square each number and sum it.
    print(total_score)


word=input("Enter the input word [all upper case]:")
score_calculation(word)

