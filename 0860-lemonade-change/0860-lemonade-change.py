class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        my_dict = {5:0,10:0,20:0}
        for i in range(len(bills)):
            if bills[i] == 5:
                my_dict[bills[i]] += 1
            elif bills[i] == 10:
                if my_dict[5] == 0:
                    return False
                else:
                    my_dict[5] -= 1
                    my_dict[bills[i]] += 1
            else:
                my_dict[bills[i]] += 1
                if my_dict[10] != 0 and my_dict[5] != 0:
                    my_dict[10] -= 1
                    my_dict[5] -= 1
                elif my_dict[10] == 0 and my_dict[5] >= 3:
                    my_dict[5] -= 3
                else:
                    return False
        return True
        