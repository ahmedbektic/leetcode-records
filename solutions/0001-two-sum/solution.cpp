class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> solution;

        int len = nums.size();

        for (int i=0; i<len; i++) {
            for (int j=0; j<len; j++) {
                if (nums.at(i)+nums.at(j) == target) {
                    if (i != j) {
                        solution.push_back(i);
                        solution.push_back(j);

                        return solution;
                    }
                }
            }
        }

        return solution;
    }
};
