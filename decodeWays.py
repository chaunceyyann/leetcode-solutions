#!/bin/python
#############
# O(n)
class Solution {
public:
int numDecodings(string s) {
    if(s.empty()) return 0;
    vector<int> dp(s.size()+1,0);
    dp[0] = 1;
    if(s[0] != '0') {dp[1] = 1;}
    
    for(int i = 2; i < dp.size(); ++i){
        int j = i - 1;
        if(s[j] - '0' > 0){dp[i] += dp[i-1];}
        int two = (s[j-1] - '0')*10 + (s[j] - '0');
        if(two >= 10 && two <= 26){dp[i] += dp[i-2];}
    }
    return dp[s.size()];
}
};
#############
# O(1)
class Solution {
public:
int numDecodings(string s) {
    if(s.empty()) return 0;
    vector<int> dp(s.size()+1,0);
    int ptr0 = 1;
    int ptr1 = s[0] != '0' ? 1 : 0;

    for(int i = 2; i < dp.size(); ++i){
        int cur = 0;
        if(s[i-1] - '0' > 0){cur += ptr1;}
        int two = (s[i - 2] - '0')*10 + (s[i-1] - '0');
        if(two >= 10 && two <= 26){cur += ptr0;}
        ptr0 = ptr1;
        ptr1 = cur;
    }
    return ptr1;
}
};


