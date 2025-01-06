class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int indexer = digits.size() - 1;
        bool carry = true;
        while (carry) {
            if (digits[indexer] == 9) {
                digits[indexer] = 0;
                if (indexer == 0) {
                    digits.insert(digits.begin(), 1);
                    carry = false;
                }
                else indexer--;
            }
            else {
                digits[indexer]++;
                carry = false;
            }
        }
        return digits;
    }
};
