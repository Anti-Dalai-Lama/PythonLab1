"""В предложении все слова начинаются с различных букв. Напечатать (если можно) слова предложения в таком порядке, чтобы последняя буква каждого слова совпадала с первой буквой следующего слова."""


class SentenceCreator (object):

    class LastWordError (Exception): #только у одного слова могут совпадать первая и последняя буквы - у последнего
        def __init__(self, lastword, tryword):
            self.lastword = lastword
            self.tryword = tryword

        def __str__(self):
            return "'{0}' can't be the last word because you already have one ('{1}')".format(self.tryword, self.lastword)

    class FirstLetterError (Exception): #первая буква у каждого слова уникальна
        def __init__(self, word):
            self.word = word

        def __str__(self):
            return "You already have a word with the first letter '{0}'".format(self.word[0])

    class UnallowedWordsSequence (Exception): #первая буква у каждого слова уникальна
        def __str__(self):
            return "You can't create a needed sentence with these words"


    letter_dict = dict()
    words = list()

    def __init__(self, sentence):
        self.words = sentence.split()

    def form_dict(self):
        last_word = ""
        for i in range(0, len(self.words)):
            word = self.words[i]
            if (word[0] == word[-1] and last_word == ""):
                last_word = word
            elif (word[0] == word[-1]):
                raise SentenceCreator.LastWordError(last_word, word)

            if (word[0] not in self.letter_dict):
                self.letter_dict[word[0]] = [1, 0, word]
            elif (self.letter_dict[word[0]][0] == 0):
                self.letter_dict[word[0]] = [1, self.letter_dict[word[0]][1], word]
            else:
                raise SentenceCreator.FirstLetterError(word)

            if (word[-1] not in self.letter_dict):
                self.letter_dict[word[-1]] = [0, 1]
            else:
                self.letter_dict[word[-1]][1] += 1

    def create_sentence(self):
        zero_flag = 0
        zero_letter = self.words[0][0]

        for letter in self.letter_dict:
            if(self.letter_dict[letter][1] == 0):
                zero_flag += 1
                zero_letter = letter
            print(letter + " " + self.letter_dict[letter].__str__())

        if(zero_flag > 1):
            raise SentenceCreator.UnallowedWordsSequence()

        result_sentence = self.letter_dict[zero_letter][2]

        for i in range(1, len(self.words)):
            result_sentence += " " + self.letter_dict[result_sentence[-1]][2]

        return result_sentence

sc = SentenceCreator("ворк я лово бав кокол оля")
sc.form_dict()
print(sc.create_sentence())