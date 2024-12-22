class Solution {
public:
    bool isValid(string s) {
    std::stack<char> testStack;
    for (unsigned int i=0; i<s.length(); i++) {
        if (std::string("([{").find(s[i]) != std::string::npos) { 
            //creates a string "({[" and checks if s[i] in...
            //std::string::npos is returned if the s[i] is not found
            testStack.push(s[i]);
        }
        else if (std::string(")]}").find(s[i]) != std::string::npos) {
            //if s[i] is a closing parenthesis...
            if ( !testStack.empty() &&
                 (  (s[i] == ')' && testStack.top() == '(') ||
                    (s[i] == ']' && testStack.top() == '[') ||
                    (s[i] == '}' && testStack.top() == '{') 
                 )
                 ) {
                    testStack.pop();
                 }
            else {
                return false; //return false if mismatched bracket
            }
        }
        else {
            return false; //return false if invalid character
        }
    }
    return testStack.empty(); //if stack is empty its valid
    }
};
