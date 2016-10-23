"""В предложении все слова начинаются с различных букв. Напечатать (если можно) слова предложения в таком порядке, чтобы последняя буква каждого слова совпадала с первой буквой следующего слова."""


class SentenceCreator (object):

    class LastWordError (Exception):  # only the last word of sentence can have equal first and last symbol
        def __init__(self, lastword, tryword):
            self.lastword = lastword
            self.tryword = tryword

        def __str__(self):
            return "'{0}' can't be the last word because you already have one ('{1}')".format(self.tryword, self.lastword)

    class FirstLetterError (Exception):  # first letter of each word must be unique
        def __init__(self, word):
            self.word = word

        def __str__(self):
            return "You already have a word with the first letter '{0}'".format(self.word[0])

    class UnallowedWordsSequence (Exception):  # wrong sequence to create allowed sentence
        def __str__(self):
            return "You can't create a needed sentence with these words"

    letter_dict = dict()  # dict with special structure ['b' : [1,1,'bear']]
    words = list()  # list of words from sentence

    def __init__(self, sentence):
        self.words = sentence.split()

    def form_dict(self):  # O(n)
        last_word = ""
        for word in self.words:
            if (word[0] == word[-1] and last_word == ""):  # checking if it is the last word
                last_word = word
            elif (word[0] == word[-1]):  # if the last word has already been found
                raise SentenceCreator.LastWordError(last_word, word)

            if (word[0] not in self.letter_dict):  # if the first letter of the word wasn't found in previous words as the first letter
                self.letter_dict[word[0]] = [1, 0, word]
            elif (self.letter_dict[word[0]][0] == 0):  # if the first letter of the word was found in previous words as the last letter
                self.letter_dict[word[0]] = [1, self.letter_dict[word[0]][1], word]
            else:  # if word with the same first letter already exists
                raise SentenceCreator.FirstLetterError(word)

            # checking the last letter
            if (word[-1] not in self.letter_dict):
                self.letter_dict[word[-1]] = [0, 1]
            else:
                self.letter_dict[word[-1]][1] += 1


    def create_sentence(self):  # O(n)
        zero_flag = 0
        zero_letter = self.words[0][0]  # storing the 1-st letter of the 1-st of the sentence

        for letter in self.letter_dict:  # checking if there are more than 1 first words
            if(self.letter_dict[letter][1] == 0):
                zero_flag += 1
                zero_letter = letter
            print(letter + " " + self.letter_dict[letter].__str__())

        if(zero_flag > 1):  # the 2-nd column in dict can have one '0' max (for the 1-st word), or zero for cycle
            raise SentenceCreator.UnallowedWordsSequence()

        # start to form the sentence
        result_sentence = self.letter_dict[zero_letter][2]
        for i in range(1, len(self.words)):
            result_sentence += " " + self.letter_dict[result_sentence[-1]][2]

        return result_sentence

sc = SentenceCreator("ворк я лово бав кокол оля")
sc.form_dict()
print(sc.create_sentence())