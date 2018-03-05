#Given a set of distinct integers, S, return all possible subsets.
#
# Note:
#Elements in a subset must be in non-descending order.
#The solution set must not contain duplicate subsets.
#Also, the subsets should be sorted in ascending ( lexicographic ) order.
#The list is not necessarily sorted.
#Example :
#
#If S = [1,2,3], a solution is:
#[
#  [],
#  [1],
#  [1, 2],
#  [1, 2, 3],
#  [1, 3],
#  [2],
#  [2, 3],
#  [3],
#]
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        def mysubset(segment,idx,o_list,i_list):
            if idx+1 <= len(i_list) - 1:
                segment_new = segment[0:]
                segment_new.append(i_list[idx+1])
                o_list.append(segment_new)
                o_list = mysubset(segment_new,idx+1,o_list,i_list)
                if idx+2 <= len(i_list) -1:
                    for i in range(idx+2,len(i_list)):
                        segment_new = segment[0:]
                        segment_new.append(i_list[i])
                        o_list.append(segment_new)
                        o_list = mysubset(segment_new,i,o_list,i_list)
            return o_list
        o_list = []
        o_list.append([])
        if len(A) == 0:
            return o_list
        A = sorted(A)
        for i in range(len(A)):
            o_list.append([A[i]])
            segment = []
            segment.append(A[i])
            o_list = mysubset(segment,i,o_list,A)
        return o_list
