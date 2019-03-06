import State
class AStar:
    def __init__(self, start, hmode):
        self.hmode = hmode
        self.S0 = State.State(start, 'None')
        self.Open = []
        self.Open.append(self.S0)
        self.Closed = []
        self.G = []
        self.G.append(self.S0)
        self.result = 0
        self.step = 0
        self.post = []
    
    def run(self):
        if not self.check():
            print("Can NOT reach!", end=' ')
            return False

        while True:
            self.step += 1
            self.loop()
            if self.result == 2:
                # print("Step:", step, end=' ')
                end = self.Closed.pop()
                print("Path:")
                path = []
                path.append(end)
                while not isinstance(path[-1].father, str):
                    path.append(path[-1].father)
                path.reverse()
                for node in path:
                    print(node.table, "f(n):", node.f(self.hmode))

                '''
                print("f*(S0):", len(path)-1)
                for node in self.post:
                    print(node.f2, end=' ')
                '''
                break
            elif self.result == 1:
                print("Failed.")
                break

    def loop(self):
        print("Step: ", self.step)
        print("Len of Open: ", len(self.Open))
        print("Len of G: ", len(self.G))
        if len(self.Open) == 0:
            self.result = 1
            return
        # print("The best node:")
        n = self.Open.pop()
        self.post.append(n)
        n.printtable()
        print("The f(n) of this node:", n.f(self.hmode))
        print()
        self.Closed.append(n)
        if n.h1 == 0:
            self.result = 2
            return
            
        M = n.M()
        for P in M:
            flag = 0
            for g in self.G:
                if g.table == P.table:
                    flag = 1
                    if g.h1 > P.h1:
                        g.father = n
                        break
            if flag == 0:
                '''
                if not n.h1 <= P.h1 + 1:
                    print("!!!!!!!!!!!!")
                '''
                i = 0
                for open in self.Open:
                    if P.f(self.hmode) >= open.f(self.hmode):
                        break
                    else:
                        i += 1
                self.Open.insert(i, P)
                self.G.append(P)

    def check(self):
        spread = self.G[0].table[0] + self.G[0].table[1] + self.G[0].table[2]
        s = 0
        for i in range(len(spread)):
            if spread[i] != 0:
                for j in range(i):
                    if spread[j] != 0:
                        if spread[j] < spread[i]:
                            s += 1
        if s % 2 == 0:
            return False
        else:
            return True

