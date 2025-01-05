class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int first = 0;
        int second = 0;
        vector<int> answer;
        answer.reserve(2);

        for (int i=0; i<nums.size(); i++) {
            for (int j=0; j<nums.size(); j++) {
                if (nums[i]+nums[j] == target && i != j) {
                    answer.emplace_back(i);
                    answer.emplace_back(j);
                    return answer;
                }
            }
        }

        return answer;
    }
};
