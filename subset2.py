#Given a collection of integers that might contain duplicates, S, return all possible subsets.
#
# Note:
#Elements in a subset must be in non-descending order.
#The solution set must not contain duplicate subsets.
#The subsets must be sorted lexicographically.
#Example :
#If S = [1,2,2], the solution is:
#
#[
#[],
#[1],
#[1,2],
#[1,2,2],
#[2],
#[2, 2]
#]
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, A):
        def mysubset(segment,idx,o_list,i_list,mydict):
            if idx+1 <= len(i_list) - 1:
                segment_new = segment[0:]
                segment_new.append(i_list[idx+1])
                if mydict.get(str(segment_new)):
                    temp = 1
                else:
                    o_list.append(segment_new)
                    mydict[str(segment_new)] = 1
                o_list = mysubset(segment_new,idx+1,o_list,i_list,mydict)
                if idx+2 <= len(i_list) -1:
                    for i in range(idx+2,len(i_list)):
                        segment_new = segment[0:]
                        segment_new.append(i_list[i])
                        if mydict.get(str(segment_new)):
                            temp = 1
                        else:
                            o_list.append(segment_new)
                            mydict[str(segment_new)] = 1
                        o_list = mysubset(segment_new,i,o_list,i_list,mydict)
            return o_list
        o_list = []
        mydict = {}
        o_list.append([])
        if len(A) == 0:
            return o_list
        A = sorted(A)
        for i in range(len(A)):
            if mydict.get(str(A[i])):
                temp = 0
            else:
              o_list.append([A[i]])
              mydict[str(A[i])] = 1
            segment = []
            segment.append(A[i])
            o_list = mysubset(segment,i,o_list,A,mydict)
        return o_list 
