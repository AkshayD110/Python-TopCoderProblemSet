from collections import Counter

def score_calculation(word):
    word_cntr=Counter(list(word))
    score_list=list(word_cntr.values())
    total_score=sum([(x*x) for x in score_list]) #list comprehension to square each number and sum it.
    print(total_score)

def best_change(word):
    '''Implement the logic to change the letter to get best score'''
    pass


word=input("Enter the input word [all upper case]:")
score_calculation(word)

