class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
   
        unordered_map<int,int> possibleSol;
        vector<int> answer;
        
        //Loop through number vectors
        for(int i = 0; i < nums.size(); i++){
            int sub = target - nums[i];
             
            if(possibleSol.find(sub) != possibleSol.end()){
                answer.push_back(possibleSol[sub]); 
                answer.push_back(i);  
            }else{
                possibleSol.insert({nums[i], i});
            }
            
        }
        //Returning answer
        return answer;
    }
};