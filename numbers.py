len_global = 3

def num(n, len_ = 3):
    return [n for i in range(len_)]

numbers = {"0":[*num(1, len_global),
                *num(1, len_global),
                *num(1, len_global),
                *num(1, len_global),
                *num(1, len_global),
                *num(1, len_global),
                *num(0, len_global)],
           "1":[*num(0, len_global),
                *num(0, len_global),
                *num(1, len_global),
                *num(1, len_global),
                *num(0, len_global),
                *num(0, len_global),
                *num(0, len_global)],
           "2":[*num(1, len_global),
                *num(1, len_global),
                *num(0, len_global),
                *num(1, len_global),
                *num(1, len_global),
                *num(0, len_global),
                *num(1, len_global)],
           "3":[*num(0, len_global),
                *num(1, len_global),
                *num(1, len_global),
                *num(1, len_global),
                *num(1, len_global),
                *num(0, len_global),
                *num(1, len_global)],
           "4":[*num(0, len_global),
                *num(0, len_global),
                *num(1, len_global),
                *num(1, len_global),
                *num(0, len_global),
                *num(1, len_global),
                *num(1, len_global)],
           "5":[*num(0, len_global),
                *num(1, len_global),
                *num(1, len_global),
                *num(0, len_global),
                *num(1, len_global),
                *num(1, len_global),
                *num(1, len_global)],
           "6":[*num(1, len_global),
                *num(1, len_global),
                *num(1, len_global),
                *num(0, len_global),
                *num(1, len_global),
                *num(1, len_global),
                *num(1, len_global)],
           "7":[*num(0, len_global),
                *num(0, len_global),
                *num(1, len_global),
                *num(1, len_global),
                *num(1, len_global),
                *num(0, len_global),
                *num(0, len_global)],
           "8":[*num(1, len_global),
                *num(1, len_global),
                *num(1, len_global),
                *num(1, len_global),
                *num(1, len_global),
                *num(1, len_global),
                *num(1, len_global)],
           "9":[*num(0, len_global),
                *num(1, len_global),
                *num(1, len_global),
                *num(1, len_global),
                *num(1, len_global),
                *num(1, len_global),
                *num(1, len_global)]}
