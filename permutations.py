#Given a collection of numbers, return all possible permutations.
#
#Example:
#
#[1,2,3] will have the following permutations:
#
#[1,2,3]
#[1,3,2]
#[2,1,3] 
#[2,3,1] 
#[3,1,2] 
#[3,2,1]
# NOTE
#No two entries in the permutation sequence should be the same.
#For the purpose of this problem, assume that all the numbers in the collection are unique.
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        def permutations(my_str):
            if len(my_str) == 1:
                return [my_str]
            all_perms = permutations(my_str[1:])
            first_char = my_str[0]
            output = []
            for i in all_perms:
                for j in range(len(i)+1):
                    output.append(i[:j]+first_char+i[j:])
            return output
        if len(A) == 1:
            return [A]
        A_str = ''.join(str(x) for x in A)
        permutations_str = permutations(A_str)
        perm_list = []
        for i in range(len(permutations_str)):
            perm_list.append([])
            for j in range(len(permutations_str[i])):
                perm_list[i].append(int(permutations_str[i][j]))
        return perm_list
