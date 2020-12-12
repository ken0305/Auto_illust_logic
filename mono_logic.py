import numpy as np


def ready_num():
    ll_row = []
    ll_column = []
    rnum = int(input('row : '))
    cnum = int(input('column : '))
    # 行方向の数字の読み込み
    i = 0
    while True:
        rows = input('row number (from top) : ')
        l_row = rows.split(',')
        l_row = [int(n) for n in l_row]
        ll_row.append(l_row)
        i += 1
        if i == rnum:
            break
    # 列方向の数字の読み込み
    i = 0
    while True:
        columns = input('column number (from left) : ')
        l_column = columns.split(',')
        l_column = [int(n) for n in l_column]
        ll_column.append(l_column)
        i += 1
        if i == cnum:
            break
    return ll_row, ll_column, rnum, cnum


def try_1(ll_row, ll_column, sheet, rnum, cnum):
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
                sheet[i, :] = 1
            else:
                j = 0
                for column in l_column:
                    sheet[i, j:column] = 1
                    j += column
                    sheet[i, j] = -1
                    j += 1


def try_2(ll_row, ll_column, sheet, rnum, cnum):
    for l_row in ll_row:
        nmax = max(l_row)
        total = sum(l_row) + len(l_row) - 1
        if total < rnum and nmax > (rnum - total):
            l_left = []
            l_right = []
            for i in range(len(l_row)):
                l_left.extend([i] * l_row[i])
                if i != len(l_row) - 1:
                    l_left.append(-1)
            for i in reversed(range(len(l_row))):
                l_in = [i] * l_row[i]


def main():
    ll_row, ll_column, rnum, cnum = ready_num()
    sheet = np.zeros(rnum * cnum).reshape(rnum, cnum)
    try_1(ll_row, ll_column, sheet)




if __name__ == '__main__':
    main()
