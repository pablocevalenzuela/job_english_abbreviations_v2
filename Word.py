class Word:

    en_words_abbre = {
        "ASAP": "As soon as possible.",
        "TBC": "To be confirmed.",
        "TBD": "To be discussed.",
        "FYI": "For you information.",
        "FAQ": "requently asked question.",
        "DM": "Direct message.",
        "PS": "Postscript.",
        "SWOT": "Strengths, weaknesses, opportunities, threats."
        }
    
    def __init__(self):
        self = self

    def search_word(self, word):
        param_word = word

        if param_word in self.en_words_abbre:
            print("It's meaning " + self.en_words_abbre.get(param_word))
        else:
            print("Doesn't exist")
    
    
word = Word()
word.search_word("ASAP")        
    
    #print(en_words_abbre.get("ASAP"))