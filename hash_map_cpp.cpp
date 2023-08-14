/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
*/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> dp;
        vector<int> ans;
        for(int i = 0; i < nums.size(); i++) {
            if(dp[target - nums[i]]) {
                ans.push_back(i);
                ans.push_back(dp[target - nums[i]] - 1);
                break;
            } 
            else {
                dp[nums[i]] = i+1;
            }
        }
        return ans;
    }
};