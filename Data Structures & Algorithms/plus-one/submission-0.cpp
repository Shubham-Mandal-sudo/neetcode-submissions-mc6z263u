class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        bool flag = true;
        int i = digits.size()-1;
        while(flag){
            if(i == -1){
                digits.insert(digits.begin(),1);
                break;
            }
            digits[i] += 1;
            if(digits[i] == 10){
                digits[i] = 0;
            }
            else{
                break;
            }
            i--; 
        }
        return digits;
    }
};
