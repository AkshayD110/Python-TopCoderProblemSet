from collections import Counter

def score_calculation(word):
    '''Below two conditiopns to check inputs validations'''
    if (len(word)>50):
        raise ValueError("The length of input word should be with in 50characters")
    if (word.islower()):
        raise ValueError("The word should be in upper case")
    word_cntr=Counter(list(word))
    print(word_cntr)
    score_list=list(word_cntr.values())
    total_score=sum([(x*x) for x in score_list]) #list comprehension to square each number and sum it.
    print(total_score)

def best_change(word):
    '''Implement the logic to change the letter to get best score'''

    pass


word=input("Enter the input word [all upper case]:")
score_calculation(word)

