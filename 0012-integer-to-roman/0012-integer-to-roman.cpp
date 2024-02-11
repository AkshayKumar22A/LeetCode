class Solution {
public:
    string intToRoman(int num) {

        vector<string> sym = {"M",  "CM", "D",  "CD", "C",  "XC", "L",
                              "XL", "X",  "IX", "V",  "IV", "I"};
        vector<int> val = {1000, 900, 500, 400, 100, 90, 50,
                           40,   10,  9,   5,   4,   1};

        string res = "";

        for (int i = 0; i < sym.size(); i++) {
            if (num != 0) {
                int num_of_time_repeated = num / val[i];
                if (num_of_time_repeated != 0) {
                    for (int k = 0; k < num_of_time_repeated; k++)
                        res += sym[i];
                    num = num % val[i];
                }
            }
        }
        return res;
    }
};