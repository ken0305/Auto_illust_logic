def main():
    ll_row = []
    ll_column = []
    row = input('row : ')
    column = input('column : ')
    i = 0
    while True:
        rows = input('row number : ')
        l_row = rows.split(',')
        l_row = [int(n) for n in l_row]
        ll_row.append(l_row)
        i += 1
        if i == row:
            break
    i = 0
    while True:
        columns = input('column number : ')
        l_column = columns.split(',')
        l_column = [int(n) for n in l_column]
        ll_column.append(l_column)
        i += 1
        if i == column:
            break


if __name__ == '__main__':
    main()
