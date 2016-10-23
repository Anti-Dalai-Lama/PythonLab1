"""Шифр "Перевернутые группы". Дан текст. Осуществить шифрование и дешифрование следующим образом: текст разбивается
на группы из k элементов, в каждой группе символы переставляются некоторым образом
(например, записываются в обратном порядке), далее переставляются сами группы символов."""


class ReversedEncryption(object):
    text = ""
    text_len = 0
    blocks_sequence = ""
    block_len = 0
    elements_sequence = ""
    list_letters = list()

    def __init__(self, message, blocks_seq, elements_seq):
        self.text = message
        self.text_len = len(message)
        self.blocks_sequence = list(map(int, blocks_seq.split()))
        self.elements_sequence = list(map(int, elements_seq.split()))
        self.block_len = len(self.elements_sequence)

    def encrypt(self):
        self.list_letters.clear()
        if(self.text_len != len(self.blocks_sequence) * len(self.elements_sequence)):
            raise Exception("Can't divide message on blocks")

        for gr_num in self.blocks_sequence:
            for el_num in self.elements_sequence:
                pos = self.block_len * gr_num + el_num
                self.list_letters.append(self.text[pos])

        return ''.join(self.list_letters)

    def decrypt(self):
        self.list_letters.clear()
        if (self.text_len != len(self.blocks_sequence) * len(self.elements_sequence)):
            raise Exception("Can't divide message on blocks")

        temp_list = []
        for i in range(0, self.text_len // self.block_len):
            temp_list.append(i)


        gr_counter = 0
        for gr_num in self.blocks_sequence:
            temp_list[gr_num] = []
            el_counter = 0
            for i in range(0, self.block_len):
                temp_list[gr_num].append(i)
            for el_num in self.elements_sequence:
                temp_list[gr_num][el_num] = self.text[gr_counter * self.block_len + el_counter ]
                el_counter += 1
            gr_counter += 1
            temp_list[gr_num] = ''.join(str(x) for x in temp_list[gr_num])
        return ''.join(temp_list)


crypto = ReversedEncryption("012345678", "1 0 2", "1 2 0")
enc = crypto.encrypt()
print(enc)
crypto = ReversedEncryption("453120786", "1 0 2", "1 2 0")
dec = crypto.decrypt()
print(dec)

crypto = ReversedEncryption("abcdefghijklmnopqrst", "9 8 7 6 5 4 3 2 0 1", "1 0")
enc = crypto.encrypt()
print(enc)
crypto = ReversedEncryption("tsrqponmlkjihgfebadc", "9 8 7 6 5 4 3 2 0 1", "1 0")
dec = crypto.decrypt()
print(dec)


crypto = ReversedEncryption("abcdefghijklmno", "2 0 3 4 1", "1 0 2")
enc1 = crypto.encrypt()
print(enc1)
crypto = ReversedEncryption("hgibackjlnmoedf", "2 0 3 4 1", "1 0 2")
dec = crypto.decrypt()
print(dec)