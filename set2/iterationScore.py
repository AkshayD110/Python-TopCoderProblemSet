class iterationScore(object):
    def __init__(self, word1, word2):
        self.word1 = word1
        self.word2 = word2

    def __repr__(self):
        return f'This {self.__class__.__name__} calculates the score of the iterations'
    @property
    def word1(self):
        return self._word1

    @word1.setter
    def word1(self, word1):
        self._word1 = word1

    @property
    def word2(self):
        return self._word2

    @word2.setter
    def word2(self, word2):
        self._word2 = word2


    def score_calculator(self):
        #write the score calcutaion logic here
        word1_ls=list(self.word1)
        word2_ls=list(self.word2)
        word1_ls.sort()
        word2_ls.sort()
        #print(f"I am word1 = {word1_ls}")
        #print(f"I am word2 = {word2_ls}")
        for i in range(len(word1_ls)):
            #logic to comapare and change the score
	    char1_ord = ord('word1_ls[i]')
	    char2_ord = ord('word2_ls[i]')
