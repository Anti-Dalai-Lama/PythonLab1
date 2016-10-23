"""Шифр "Перевернутые группы". Дан текст. Осуществить шифрование и дешифрование следующим образом: текст разбивается
на группы из k элементов, в каждой группе символы переставляются некоторым образом
(например, записываются в обратном порядке), далее переставляются сами группы символов."""


class TurningEncryption(object):
    text = ""
    text_len = 0
    blocks_sequence = ""  # sequence of blocks in message
    block_len = 0
    elements_sequence = ""  # sequence of elements in block
    list_letters = list()  # string is being built here

    def __init__(self, message, blocks_seq, elements_seq):
        self.text = message
        self.text_len = len(message)
        self.blocks_sequence = list(map(int, blocks_seq.split()))
        self.elements_sequence = list(map(int, elements_seq.split()))
        self.block_len = len(self.elements_sequence)

        # check if we can divide text into blocks of assigned length
        if (self.text_len != len(self.blocks_sequence) * len(self.elements_sequence)):
            raise Exception("Can't divide message on blocks")

    def encrypt(self):  #O(n)
        self.list_letters.clear()
        for gr_num in self.blocks_sequence:
            for el_num in self.elements_sequence:
                pos = self.block_len * gr_num + el_num  # getting a position of current symbol to input in result
                self.list_letters.append(self.text[pos])  # decided to avoid string concatenation (memory issues)
        return ''.join(self.list_letters) # getting string from list

    def decrypt(self):  #O(n)
        self.list_letters.clear()
        for i in range(0, self.text_len // self.block_len):  # creating empty list to store blocks and elements [[],[]]
            temp = list()
            for k in range(0, self.block_len):
                temp.append(k)
            self.list_letters.append(temp)

        el_counter = 0  # counter for current element
        for gr_num in self.blocks_sequence:
            for el_num in self.elements_sequence:
                # write symbol with current position in needed cell
                self.list_letters[gr_num][el_num] = self.text[el_counter]
                el_counter += 1
            self.list_letters[gr_num] = ''.join(self.list_letters[gr_num]) # decided to avoid string concatenation
        return ''.join(self.list_letters)


message = "012345678"
groups_seq = "1 0 2"
elements_seq = "1 2 0"

# message = "abcdefghijklmnopqrst"
# groups_seq = "9 8 7 6 5 4 3 2 0 1"
# elements_seq = "1 0"

# message = "abcdefghijklmno"
# groups_seq = "2 0 3 4 1"
# elements_seq = "1 0 2"

crypto = TurningEncryption(message, groups_seq, elements_seq)
enc = crypto.encrypt()
print(enc)
crypto = TurningEncryption(enc, groups_seq, elements_seq)
dec = crypto.decrypt()
print(dec)
