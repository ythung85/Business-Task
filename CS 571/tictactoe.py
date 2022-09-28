import numpy as np
import time
import sys
import argparse

class TicTacToe():
    def __init__(self, n, k, order):
        self.n = n
        self.k = k
        self.order = order
        self.startgame()
        
    def startgame(self):
        self.state = np.array(['.']*(self.n**2)).reshape(self.n,self.n)
        #self.state = [['.','.','.'],
                      #['.','.','.'],
                      #['.','.','.']]
                
        self.first = self.order[0]
        
    def board(self):
        
        for i in range(0, self.n):
            for j in range(0, self.n):
                print('{}|'.format(self.state[i][j]), end=" ")
            print()
        print()
        
    def end_game(self):
        
        k = self.k
        n = self.n
        #v
        
        
        for i in range(0,n):
            for j in range(0,n-k+1):
                if self.state[i][j] != '.' and np.count_nonzero(self.state[i,j:j+k] == self.state[i][j]) == k:
                    return self.state[i][j]
        
        for i in range(0,n-k+1):
            for j in range(0,n):
                if self.state[i][j] != '.' and np.count_nonzero(self.state[i:i+k,j] == self.state[i][j]) == k:
                    return self.state[i][j]
        
        # pos dig
        for i in range(0,n-k+1):
            cur = []
            for j in range(0, n):
                if(i < n and j < n):
                    cur.append(self.state[i,j])
                    i+=1
            for z in range(len(cur)-k+1):
                if cur[z] != '.' and np.count_nonzero(np.array(cur[z:z+k]) == cur[z]) == k:
                    return (cur[z])

        for j in range(1,n-k+1):
            cur = []
            for i in range(0, n):
                if(i < n and j < n):
                    cur.append(self.state[i,j])
                    j+=1
            for z in range(len(cur)-k+1):
                if cur[z] != '.' and np.count_nonzero(np.array(cur[z:z+k]) == cur[z]) == k:
                    return (cur[z])
            
        # neg dig
        for i in range(0,n-k+1):
            cur = []
            for j in range(n-1, -1, -1):
                if(i < n and j < n):
                    cur.append(self.state[i,j])
                    i+=1
            for z in range(len(cur)-k+1):
                if cur[z] != '.' and np.count_nonzero(np.array(cur[z:z+k]) == cur[z]) == k:
                    return(cur[z])

        for j in range(1,n-k+1):
            cur = []
            for i in range(n-1, -1, -1):
                if(i < n and j < n):
                    cur.append(self.state[i,j])
                    j+=1
            for z in range(len(cur)-k+1):
                if cur[z] != '.' and np.count_nonzero(np.array(cur[z:z+k]) == cur[z]) == k:
                    return(cur[z])

        
        '''
        for i in range(0,n-k+1):
            if np.diag(self.state)[i] != '.' and np.count_nonzero(np.diag(self.state)[i:i+k] == np.diag(self.state)[i]) == k:
                return np.diag(self.state)[i]
            
        for i in range(0,n-k+1):
            if np.diag(np.fliplr(self.state))[i] != '.' and np.count_nonzero(np.diag(np.fliplr(self.state))[i:i+k] == np.diag(np.fliplr(self.state))[i]) == k:
                return np.diag(np.fliplr(self.state))[i]
        '''
        for i in range(n):
            for j in range(n):
                if self.state[i][j] == '.':
                    return None
        
        
        return '.'

    def minimum(self, a, b):
        minv = np.inf
        xxx = 0
        yyy = 0

        if self.end_game() == 'x':
            return (-1, 0, 0)
        elif self.end_game() == 'o':
            return (1,0,0)
        elif self.end_game() == '.':
            return (0,0,0)


        ## 3x3

        # x turn
        for i in range(self.n):
            for j in range(self.n):
                if self.state[i][j] == '.':
                    self.state[i][j] = 'x'
                    (v, min_i,min_j) = self.maximum(a, b)

                    if v < minv:
                        minv = v
                        xxx = i
                        yyy = j

                    self.state[i][j] = '.'

                    if minv <= a:
                        return (minv, xxx, yyy)

                    if minv < b:
                        b = minv

        return (minv, xxx, yyy)

    def maximum(self, a, b):
        maxv = -np.inf

        xx = 0
        yy = 0

        if self.end_game() == 'x':
            return (-1, 0, 0)
        elif self.end_game() == 'o':
            return (1,0,0)
        elif self.end_game() == '.':
            return (0,0,0)
        ## 3x3

        # x turn
        
        for i in range(self.n):
            for j in range(self.n):
                if self.state[i][j] == '.':
                    self.state[i][j] = 'o'
                    (v, max_i,max_j) = self.minimum(a, b)
                    if v > maxv:
                        maxv = v
                        xx = i
                        yy = j

                    self.state[i][j] = '.'

                    if maxv >= b:
                        return (maxv, xx, yy)
                    if maxv > a:
                        a = maxv

        return (maxv, xx, yy)
    
    def play_alpha_beta(self):
        
        while True:
            self.board()
            self.result = self.end_game()

            if self.result != None:
                if self.result == 'x':
                    print('The winner is X!')
                elif self.result == 'o':
                    print('The winner is O!')
                elif self.result == '.':
                    print("It's a tie!")


                self.startgame()
                return

            if self.first == 'x':

                start = time.time()
                (m, qx, qy) = self.minimum(-2, 2)
                end = time.time()
                self.state[qx][qy] = 'x'
                self.first = 'o'

            else:
                (m, px, py) = self.maximum(-2, 2)
                self.state[px][py] = 'o'
                self.first = 'x'


argsn, argsk = int(sys.argv[1]), int(sys.argv[2])
argsturn = sys.argv[3]

start = time.time()
g = TicTacToe(n=argsn, k = argsk, order = argsturn)
g.play_alpha_beta()
end = time.time()
print('estimated time: ', end-start)
