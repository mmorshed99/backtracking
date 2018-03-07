#Given a string s, partition s such that every string of the partition is a palindrome.
#
#Return all possible palindrome partitioning of s.
#
#For example, given s = "aab",
#Return
#
#  [
#    ["a","a","b"]
#    ["aa","b"],
# ]
#
#    Ordering the results in the answer :
#
#    Entry i will come before Entry j if :
#
#        len(Entryi[0]) < len(Entryj[0]) OR
#        (len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR
#        *
#        *
#        *
#        (len(Entryi[0]) == len(Entryj[0]) AND … len(Entryi[k] < len(Entryj[k]))
#
#In the given example,
#["a", "a", "b"] comes before ["aa", "b"] because len("a") < len("aa")
#
class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        def is_plaindrome(A,left,right):
            if len(A) == 1:
                return 1
            if A[left] != A[right]:
                return 0
            left += 1
            right -= 1
            if left >= right:
               return 1
            return is_plaindrome(A,left,right)
            
        def plain_list(A):
            temp = []
            for i in range(len(A)):
                if is_plaindrome(A[:i+1],0,i):
                    if len(A[i+1:]) > 0:
                        my_list = plain_list(A[i+1:])
                        if len(my_list) > 0:
                            for j in range(len(my_list)):
                                temp.append([])
                                temp[len(temp)-1].append((A[:i+1]))
                                temp[len(temp)-1].extend(my_list[j])
                    else:
                        temp.append([A[:i+1]])
            return temp
            
        return plain_list(A)
