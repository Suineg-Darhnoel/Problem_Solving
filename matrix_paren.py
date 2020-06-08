import re
import math

class MatrixParen:
    def __init__(self, mat_alpha='A', mat_nums=0):
        self.matrix_list = [mat_alpha+str(i) for i in range(1, mat_nums+1)]
        self.__paren_nums = 0

    def num_index_of(self, string : str) -> int:
        for i, c in enumerate(string):
            if c.isdigit():
                return i
        return None

    def concat_mat_pair(self, fst, snd):
        # get index of the first found number in string
        fstn_i = self.num_index_of(fst)
        sndn_i = self.num_index_of(snd)

        return fst[:fstn_i] + fst[fstn_i:] + snd[sndn_i:]

    def shrink_lst(self, mat_lst, pos1, pos2):
        # new combined matrix
        new_mat = [self.concat_mat_pair(mat_lst[pos1], mat_lst[pos2])]
        return mat_lst[:pos1] + new_mat + mat_lst[pos2+1:]

    def __mat_paren_perm(self, mat_lst=None):
        if mat_lst is None:
            mat_lst = self.matrix_list
        for i in range(len(mat_lst)-1):
            j = i+1
            sl = self.shrink_lst(mat_lst, i, j)
            if len(sl) == 1:
                print(sl)
                print("-" * 20)
                self.__paren_nums += 1
            else:
                print(sl)
            self.__mat_paren_perm(sl)

    @property
    def paren_nums(self):
        self.__paren_nums = 0
        self.__mat_paren_perm()
        return self.__paren_nums


m = MatrixParen('A', 4)
print(m.paren_nums)
