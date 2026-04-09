class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int low = 0;
        int c = matrix[0].size();
        int r = matrix.size();
        int high = r*c - 1;
        while(low<=high){
            int mid = (high+low)/2;
            int temp = matrix[mid/c][mid%c];
            if(temp == target){
                return true;
            }
            else if(temp < target){
                low = mid + 1;
            }
            else{
                high = mid - 1;
            }
        }

        return false;
    }
};
