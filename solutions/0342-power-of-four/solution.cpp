class Solution {
public:
    bool isPowerOfFour(int n) {
        if (n > 4) {
            if (n % 4 != 0) {
                return false;
            }
            return isPowerOfFour(n/4);
        }
        if (n == 4 || n == 1) {
            return true;
        }
        return false;
    }
};
