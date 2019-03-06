import copy
dic1 = {(1,1):0, (0,0):1, (0,1):2, (0,2):3, (1,2):4, (2,2):5, (2,1):6, (2,0):7, (1,0):8}
dic2 = {v: k for k, v in dic1.items()}


class State:
    def __init__(self, table, father):
        self.table = table
        if not isinstance(father, str):
            self.father = father
            self.g = self.g()
            self.h1 = self.h1()
            self.h2 = self.h2()
        else:
            self.father = father
            self.g = 0
            self.h1 = self.h1()
            self.h2 = self.h2()

    def changeFather(self, father):
        self.father = father
        self.g = self.g()

    def f(self, hmode):
        if hmode == 1:
            return self.g + self.h1
        else:
            return self.g + self.h2

    def g(self):
        return self.father.g + 1

    def h1(self):
        h = 0
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                if self.table[i][j] != dic1[(i, j)]:
                    h += 1
        return h

    def h2(self):
        h = 0
        for i in range(3):
            for j in range(3):
                if self.table[i][j] == 0:
                    continue
                (r, c) = dic2[self.table[i][j]]
                h += abs(i - r) + abs(j - c)
        return h


    def M(self):
        M = []
        temp = []
        i, j = self.zero()
        if i - 1 >= 0:
            table = copy.deepcopy(self.table)
            table[i - 1][j], table[i][j] = table[i][j], table[i - 1][j]
            temp.append(table)
        if j + 1 <= 2:
            table = copy.deepcopy(self.table)
            table[i][j + 1], table[i][j] = table[i][j], table[i][j + 1]
            temp.append(table)
        if j - 1 >= 0:
            table = copy.deepcopy(self.table)
            table[i][j - 1], table[i][j] = table[i][j], table[i][j - 1]
            temp.append(table)
        if i + 1 <= 2:
            table = copy.deepcopy(self.table)
            table[i + 1][j], table[i][j] = table[i][j], table[i + 1][j]
            temp.append(table)
        for table in temp:
            p = self.father
            while True:
                if not isinstance(p, str):
                    if table == p.table:
                        break
                    p = p.father
                else:
                    s = State(table, self)
                    M.append(s)
                    break
        return M


    def zero(self):
        for i in range(3):
            for j in range(3):
                if self.table[i][j] == 0:
                    return i, j

    def printtable(self):
        for row in self.table:
            print(row)
