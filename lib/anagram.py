class Anagram:
    
    def __init__(self, word):
        self.word = word
    
    def match(self, pot_an):
        word_list = sorted(list(self.word))
        anagram_list = []
        for word in pot_an:
            if word_list == (sorted([letter for letter in word])):
                anagram_list.append(word)
        return anagram_list