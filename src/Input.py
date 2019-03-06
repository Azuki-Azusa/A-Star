import numpy
def Input(state):

    if state == 0:
        row = []
        '''
        row.append(input())
        row.append(input())
        row.append(input())
        '''
        row.append('2 8 3')
        row.append('1 6 4')
        row.append('7 0 5')
    
        row[0] = row[0].split()
        row[1] = row[1].split()
        row[2] = row[2].split()

        table = []
        for i in range(3):
            table.append([])
            for j in range(3):
                table[i].append(int(row[i][j]))
        # print(table)

    if state == 1:
        num = []
        for i in range(9):
            num.append(i)
        num = numpy.random.permutation(num)
        # print(num)
        table = []
        for i in range(3):
            table.append([])
            for j in range(3):
                table[i].append(num[i * 3 + j])
        print(table)


    return table
