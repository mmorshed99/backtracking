class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    def combine(self, A, B):
        def comb(A,have,goal):
            my_ret = []
            if goal-have == 1:
                for i in A:
                    temp = [i]
                    my_ret.append(temp)
                return my_ret
            for i in range(len(A)-1):
                temp = comb(A[i+1:],have+1,goal)
                for j in temp:
                    save = [A[i]]
                    save.extend(j)
                    my_ret.append(save)
            return my_ret
        my_in = []
        for i in range(1,A+1):
            my_in.append(i)
        if len(my_in) == B:
            return [my_in]
        if len(my_in) == 0:
            return [my_in]
        return comb(my_in,0,B)
