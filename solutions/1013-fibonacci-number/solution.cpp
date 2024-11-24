class Solution {
public:
    int fib(int n) {
        if (n == 0 || n == 1){
            return n;
        }
        int value1 = 0;
        int value2 = 1;
        for(int i=3; i <= n; i++) {
            int temp = value2;
            value2 += value1;
            value1 = temp;
        }
        return value1 + value2;
    }
};
