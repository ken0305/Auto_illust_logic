import numpy as np
import itertools as iter


def ready_num():
    ll_row = []
    ll_column = []
    rnum = int(input('row : '))
    cnum = int(input('column : '))
    # 行方向の数字の読み込み
    i = 0
    while True:
        rows = input('row %d number (from top) : ' % (i + 1))
        l_row = rows.split(',')
        l_row = [int(n) for n in l_row]
        ll_row.append(l_row)
        i += 1
        if i == rnum:
            break
    # 列方向の数字の読み込み
    i = 0
    while True:
        columns = input('column %d number (from left) : ' % (i + 1))
        l_column = columns.split(',')
        l_column = [int(n) for n in l_column]
        ll_column.append(l_column)
        i += 1
        if i == cnum:
            break
    return ll_row, ll_column, rnum, cnum


def check_sheet():
    for i in range(rnum):
        flg = True
        for j in range(cnum):
            if sheet[i, j] != -1 and sheet[i, j] != 1:
                flg = False
                break
        if flg:
            check['row'][i] = 1
    for i in range(cnum):
        flg = True
        for j in range(rnum):
            if sheet[i, j] != -1 and sheet[i, j] != 1:
                flg = False
                break
        if flg:
            check['column'][i] = 1


def try_1():
    for l_row, i in zip(ll_row, range(rnum)):
        total = sum(l_row) + len(l_row) - 1
        if total == rnum:
            if len(l_row) == 1:
                sheet[i, :] = 1
            else:
                j = 0
                for row in l_row:
                    sheet[i, j:row] = 1
                    j += row
                    sheet[i, j] = -1
                    j += 1
    for l_column, i in zip(ll_column, range(cnum)):
        total = sum(l_column) + len(l_column) - 1
        if total == cnum:
            if len(l_column) == 1:
                sheet[:, i] = 1
            else:
                j = 0
                for column in l_column:
                    sheet[j:column, i] = 1
                    j += column
                    sheet[j, i] = -1
                    j += 1


def try_2():
    for l_row, i in zip(ll_row, range(rnum)):
        nmax = max(l_row)
        total = sum(l_row) + len(l_row) - 1
        if total < rnum and nmax > (rnum - total):
            l_left = []
            l_right = []
            for j in range(len(l_row)):
                l_left.extend([j] * l_row[j])
                if i != len(l_row) - 1:
                    l_left.append(-1)
            for j in reversed(range(len(l_row))):
                l_right = [j] * l_row[j] + l_right
                if j != 0:
                    l_right.insert(0, -1)
            j = 0
            while True:
                if l_left[j] == l_right[j] and l_left[j] != -1 and l_right[j] != -1:
                    sheet[i, j] = 1
    for l_column, i in zip(ll_column, range(cnum)):
        nmax = max(l_column)
        total = sum(l_column) + len(l_column) - 1
        if total < cnum and nmax > (cnum - total):
            l_left = []
            l_right = []
            for j in range(len(l_column)):
                l_left.extend([j] * l_column[j])
                if i != len(l_column) - 1:
                    l_left.append(-1)
            for j in reversed(range(len(l_column))):
                l_right = [j] * l_column[j] + l_right
                if j != 0:
                    l_right.insert(0, -1)
            j = 0
            while True:
                if l_left[j] == l_right[j] and l_left[j] != -1 and l_right[j] != -1:
                    sheet[j, i] = 1


def try_3():
    # 上
    for i, l_column in zip(range(cnum), ll_column):
        if sheet[0, i] == 1:
            j = 1
            pos = 0
            num = 1
            posflg = False
            while True:
                if sheet[j, i] == 1:
                    num += 1
                elif sheet[j, i] == -1:
                    if sheet[j - 1, i] == 1:
                        pos += 1
                        posflg = True
                else:
                    if l_column[pos] > num:
                        sheet[j, i] = 1
                        num += 1
                    elif l_column[pos] == num:
                        sheet[j, i] = -1
                        num = 0
                        pos += 1
                        posflg = True
                j += 1
                if posflg:
                    if sheet[j, i] == 0:
                        break
                    elif sheet[j, i] == 1:
                        posflg = False
                if j == rnum:
                    break
        elif sheet[0, i] == -1:
            j = 1
            pos = 0
            num = 0
            posflg = False
            while True:
                if sheet[j, i] == 1:
                    num += 1
                elif sheet[j, i] == -1:
                    if sheet[j - 1, i] == 1:
                        pos += 1
                        posflg = False
                else:
                    if num == 0:
                        break
                    elif num > 0:
                        if num == l_column[pos]:
                            sheet[j, i] = -1
                            pos += 1
                            posflg = True
                        else:
                            sheet[j, i] = 1
                j += 1
                if posflg:
                    if sheet[j, i] == 0:
                        break
                    elif sheet[j, i] == 1:
                        posflg = False
                if j == rnum:
                    break
    # 下
    for i, l_column in zip(reversed(range(cnum)), ll_column):
        if sheet[rnum - 1, i] == 1:
            j = rnum - 2
            pos = len(l_column) - 1
            num = 1
            posflg = False
            while True:
                if sheet[j, i] == 1:
                    num += 1
                elif sheet[j, i] == -1:
                    if sheet[j + 1, i] == 1:
                        pos += 1
                        posflg = True
                else:
                    if l_column[pos] > num:
                        sheet[j, i] = 1
                        num += 1
                    elif l_column[pos] == num:
                        sheet[j, i] = -1
                        num = 0
                        pos -= 1
                        posflg = True
                j -= 1
                if posflg:
                    if sheet[j, i] == 0:
                        break
                    elif sheet[j, i] == 1:
                        posflg = False
                if j == -1:
                    break
        elif sheet[rnum - 1, i] == -1:
            j = rnum - 2
            pos = len(l_column) - 1
            num = 0
            posflg = False
            while True:
                if sheet[j, i] == 1:
                    num += 1
                elif sheet[j, i] == -1:
                    if sheet[j + 1, i] == 1:
                        pos -= 1
                        posflg = False
                else:
                    if num == 0:
                        break
                    elif num > 0:
                        if num == l_column[pos]:
                            sheet[j, i] = -1
                            pos -= 1
                            posflg = True
                        else:
                            sheet[j, i] = 1
                j -= 1
                if posflg:
                    if sheet[j, i] == 0:
                        break
                    elif sheet[j, i] == 1:
                        posflg = False
                if j == -1:
                    break
    # 左
    for i, l_row in zip(range(rnum), ll_row):
        if sheet[i, 0] == 1:
            j = 1
            pos = 0
            num = 1
            posflg = False
            while True:
                if sheet[i, j] == 1:
                    num += 1
                elif sheet[i, j] == -1:
                    if sheet[i, j - 1] == 1:
                        pos += 1
                        posflg = True
                else:
                    if l_row[pos] > num:
                        sheet[i, j] = 1
                        num += 1
                    elif l_row[pos] == num:
                        sheet[i, j] = -1
                        num = 0
                        pos += 1
                        posflg = True
                j += 1
                if posflg:
                    if sheet[i, j] == 0:
                        break
                    elif sheet[i, j] == 1:
                        posflg = False
                if j == cnum:
                    break
        elif sheet[i, 0] == -1:
            j = 1
            pos = 0
            num = 0
            posflg = False
            while True:
                if sheet[i, j] == 1:
                    num += 1
                elif sheet[i, j] == -1:
                    if sheet[i, j - 1] == 1:
                        pos += 1
                        posflg = False
                else:
                    if num == 0:
                        break
                    elif num > 0:
                        if num == l_row[pos]:
                            sheet[i, j] = -1
                            pos += 1
                            posflg = True
                        else:
                            sheet[i, j] = 1
                j += 1
                if posflg:
                    if sheet[i, j] == 0:
                        break
                    elif sheet[i, j] == 1:
                        posflg = False
                if j == cnum:
                    break
    # 右
    for i, l_row in zip(reversed(range(rnum)), ll_row):
        if sheet[i, cnum - 1] == 1:
            j = cnum - 2
            pos = len(l_row) - 1
            num = 1
            posflg = False
            while True:
                if sheet[i, j] == 1:
                    num += 1
                elif sheet[i, j] == -1:
                    if sheet[i, j + 1] == 1:
                        pos -= 1
                        posflg = True
                else:
                    if l_row[pos] > num:
                        sheet[i, j] = 1
                        num += 1
                    elif l_row[pos] == num:
                        sheet[i, j] = -1
                        num = 0
                        pos -= 1
                        posflg = True
                j -= 1
                if posflg:
                    if sheet[i, j] == 0:
                        break
                    elif sheet[i, j] == 1:
                        posflg = False
                if j == -1:
                    break
        elif sheet[i, cnum - 1] == -1:
            j = cnum - 2
            pos = len(l_row) - 1
            num = 0
            posflg = False
            while True:
                if sheet[i, j] == 1:
                    num += 1
                elif sheet[i, j] == -1:
                    if sheet[i, j + 1] == 1:
                        pos -= 1
                        posflg = False
                else:
                    if num == 0:
                        break
                    elif num > 0:
                        if num == l_row[pos]:
                            sheet[i, j] = -1
                            pos -= 1
                            posflg = True
                        else:
                            sheet[i, j] = 1
                j -= 1
                if posflg:
                    if sheet[i, j] == 0:
                        break
                    elif sheet[i, j] == 1:
                        posflg = False
                if j == -1:
                    break


def try_4():
    for i, l_row in zip(range(rnum), ll_row):
        if check['row'][i] == 0:
            ll_pattern = []
            posnum = len(l_row) + 1
            minum = cnum - sum(l_row)
            j = 0
            l_mipat = []
            while True:
                l_mipat.extend([j] * posnum)
                j += 1
                if j == minum + 1:
                    break
            l_mipat = list(iter.permutations(l_mipat, posnum))
            l_mipat = list(set(l_mipat))
            j = 0
            while True:
                if sum(l_mipat[j]) != minum:
                    del l_mipat[j]
                else:
                    j += 1
                if j == len(l_mipat):
                    break
            if posnum > 2:
                j = 0
                while True:
                    if 0 in l_mipat[j][1:-1]:
                        del l_mipat[j]
                    else:
                        j += 1
                    if j == len(l_mipat):
                        break
            j = 0
            while True:
                l_pattern = []
                k = 0
                while True:
                    l_pattern.extend([-1] * l_mipat[j][k])
                    l_pattern.extend([1] * l_row[k])
                    k += 1
                    if k == len(l_row):
                        break
                l_pattern.extend([-1] * l_mipat[k])
                ll_pattern.append(l_pattern)
                j += 1
                if j == len(l_mipat):
                    break


if __name__ == '__main__':
    ll_row, ll_column, rnum, cnum = ready_num()
    sheet = np.zeros([rnum, cnum])
    check = {'row': np.zeros(rnum), 'column': np.zeros(cnum)}
    try_1()
    check_sheet()
    try_2()
    check_sheet()
    try_3()
