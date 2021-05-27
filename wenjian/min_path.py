
'''
class Solution:
    """
    @param n: maximum index of position.
    @param m: the number of undirected edges.
    @param x:
    @param y:
    @param w:
    @return: return the minimum risk value.
    """

    def getMinRiskValue(end, m, x, y, w):
        axis = list(zip(x, y, w))
        min_path = []

        def myloop(start=0, log=[], danger=0):
            for each in axis:
                if each[0] == start and each[1] == end:
                    tmp = log.copy()
                    tmp.append(start)
                    tmp.append(each[1])
                    if danger < each[2]:
                        danger = each[2]
                    min_path.append((tmp, danger))
                elif each[0] == start:
                    tmp = log.copy()
                    tmp.append(start)
                    if danger < each[2]:
                        danger = each[2]
                    myloop(each[1], tmp, danger)

        myloop()
        return min_path


end, m = 5, 7
x = [0, 0, 1, 2, 3, 3, 4]
y = [1, 2, 3, 4, 4, 5, 5]
w = [2, 5, 3, 4, 3, 4, 1]
print(min(Solution.getMinRiskValue(end, m, x, y, w), key=lambda x: x[1]))


'''

'''
class Solution:
    """
    @param n: maximum index of position.
    @param m: the number of undirected edges.
    @param x:
    @param y:
    @param w:
    @return: return the minimum risk value.
    """
    def __init__(self,end, m, x, y, w):
        self.end=end
        self.x=x
        self.y=y
        self.w=w
    def getMinRiskValue(self):
        axis = list(zip(self.x, self.y, self.w))
        min_path = []
        def myloop(start=0, log=[], danger=0):
            for each in axis:
                if each[0] == start and each[1] == self.end:
                    tmp = log.copy()
                    tmp.append(start)
                    tmp.append(each[1])
                    if danger < each[2]:
                        danger = each[2]
                    min_path.append((tmp, danger))
                elif each[0] == start:
                    tmp = log.copy()
                    tmp.append(start)
                    if danger < each[2]:
                        danger = each[2]
                    myloop(each[1], tmp, danger)
        myloop()
        return min_path


end, m = 5, 7
x = [0, 0, 1, 2, 3, 3, 4]
y = [1, 2, 3, 4, 4, 5, 5]
w = [2, 5, 3, 4, 3, 4, 1]
if __name__ == '__main__':
    solution=Solution(end, m, x, y, w)
    print(min(solution.getMinRiskValue(), key=lambda x: x[1]))
'''
class Solution:
    """
    @param n: maximum index of position.
    @param m: the number of undirected edges.
    @param x:
    @param y:
    @param w:
    @return: return the minimum risk value.
    """
    # def __init__(self,end, m, x, y, w):
    #     self.end=end
    #     self.x=x
    #     self.y=y
    #     self.w=w
    def getMinRiskValue(self,n, m, x, y, w):
        axis = list(zip(x, y, w))
        min_path = []
        def myloop(start=0, log=[], danger=0):
            for each in axis:
                if each[0] == start and each[1] == n:
                    tmp = log.copy()
                    tmp.append(start)
                    tmp.append(each[1])
                    if danger < each[2]:
                        danger = each[2]
                    min_path.append((tmp, danger))
                elif each[0] == start:
                    tmp = log.copy()
                    tmp.append(start)
                    if danger < each[2]:
                        danger = each[2]
                    myloop(each[1], tmp, danger)
        myloop()
        min_pa = min(min_path, key=lambda x: x[1])
        return min_pa[1]

# end, m = 5, 7
# x = [0, 0, 1, 2, 3, 3, 4]
# y = [1, 2, 3, 4, 4, 5, 5]
# w = [2, 5, 3, 4, 3, 4, 1]

end=19
m=24
x=[0,2,8,1,15,3,14,16,18,10,0,1,2,19,8,2,0,7,14,2,17,18,15,12]
y=[19,1,10,10,8,8,7,14,11,16,12,16,16,6,7,14,8,6,0,0,4,0,4,8]
w=[82726,45109,80245,27286,56901,92031,21663,85501,57309,29121,9821,1605,60318,89465,22801,71145,97855,48145,45751,92912,68999,6651,88081,69441]
if __name__ == '__main__':
    print(Solution().getMinRiskValue(end, m, x, y, w))
