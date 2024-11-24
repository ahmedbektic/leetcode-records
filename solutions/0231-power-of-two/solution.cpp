class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n>2){
            if (n%2 != 0) {
                return false;
            }
            return isPowerOfTwo(n/2);
        }
        if (n==2 || n==1) {
            return true;
        }
        return false;
    }
};
