# -*- coding=UTF-8 -*-

idc = '230102810120103'

def idcard_convert(idcard_15):
    wi = ['7', '9', '10', '5', '8', '4', '2', '1', '6', '3', '7', '9', '10', '5', '8', '4', '2']
    ai = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    idcard_18 = '%s19%s' % (idcard_15[0:6], idcard_15[6:15])
    i = 0
    sum = 0
    for c in idcard_18:
        sum_t = int(c) * int(wi[i])
        sum += sum_t
        i += 1
    idcard_18 = '%s%s' % (idcard_18, ai[sum % 11])
    return idcard_18

if __name__ == '__main__':
    print(idc)
    print(idcard_convert(idc))
