class Solution {
public:
    int maximum69Number (int num) {
        vector<string> compare;
        stringstream ss;
        string sNum;
        ss << num;
        ss >> sNum;
        compare.push_back(sNum);
        for(int i = 0; i < sNum.length(); i++){
            
            if(sNum[i] == '6'){
                sNum[i] = '9';
                compare.push_back(sNum);
                sNum[i] = '6';
               
            }else{
                sNum[i] = '6';
                compare.push_back(sNum);  
                sNum[i] = '9';  
            }         
        }
        
        string maxNum = *max_element(compare.begin(), compare.end());
        num = stoi(maxNum);
        return num;
    }
};