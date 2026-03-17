class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0
        basket = dict()
        slow = 0
        fast = 0
        while fast < len(fruits):
            basket[fruits[fast]] = basket.get(fruits[fast],0) + 1
            if len(basket) > 2:
                basket[fruits[slow]] -= 1
                if basket[fruits[slow]] == 0:
                    del basket[fruits[slow]]
                slow += 1
            if len(basket) <= 2:
                ans = max(ans,fast-slow+1)
            fast += 1
        return ans