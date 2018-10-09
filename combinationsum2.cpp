void my_sum(vector<int>& A, int curr, int curr_sum, int sum, vector<int> temp, vector<vector<int> >& ans, map<vector<int>, bool>& m){
    
    if(curr_sum > sum){
        return;
    }  
    
    else if(curr_sum == sum){
        if(m.find(temp) == m.end()){
            m[temp] = true;
            ans.push_back(temp);
        }
        return;
    }
    
    for(int i = curr; i < A.size(); i++){
        vector<int> t(temp);
        t.push_back(A[i]);
        my_sum(A, i+1, curr_sum+A[i], sum, t, ans, m);
    }
}
vector<vector<int> > Solution::combinationSum(vector<int> &A, int B) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    vector<vector<int> > ans;
    
    int n = A.size();
    
    if(A.size() == 0){
        return ans;
    }
    
    sort(A.begin(), A.end());
    
    map<vector<int>, bool> m;
    
    for(int i = 0; i < n; i++){
        vector<int> temp;
        temp.push_back(A[i]);
        my_sum(A, i+1, A[i], B, temp, ans, m);
    }
    
    return ans;
}
