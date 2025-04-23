import math
def h_cal(list_X,number,sum):
    h_temp = 0.0
    for i in range(0,number):
        list_X.append(float(input()) / sum)
        h_temp = h_temp + (-math.log2(list_X[i]) * list_X[i])
    print(h_temp)
list_hiragana = []
list_katakana = []
h_cal(list_hiragana,10,28640)
h_cal(list_katakana,10,3708)

    