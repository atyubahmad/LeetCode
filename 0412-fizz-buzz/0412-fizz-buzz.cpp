class Solution {
public:
    vector<string> fizzBuzz(int n) {
        
        vector<string> answer;
        stringstream ss;
        
        for(int i = 1; i < n + 1; i++){
            //Converting int to string
            ss << i;
            string str = ss.str(); 
            
            //Conditions
            if(i % 3 == 0 and i % 5 == 0){
                answer.push_back("FizzBuzz");
            } else if(i % 3 == 0){
                answer.push_back("Fizz");
            } else if(i % 5 == 0){
                answer.push_back("Buzz");
            } else { 
                answer.push_back(str);
            }
            
            //Resetting string
            ss.str("");
            ss.clear();
        }
        
        return answer;
    }
};