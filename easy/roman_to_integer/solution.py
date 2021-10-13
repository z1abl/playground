nums = {
    'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000,
    'IV': 4,'IX': 9,'XL': 40,'XC': 90,'CD': 400,'CM': 900
}

class Solution:
    def romanToInt(self,s: str) -> int:
        new_int = 0
        i = 0
        while i < len(s):
            double_set = ''
            v = s[i]
            if i < len(s)-1:
                double_set = s[i] + s[i+1]
            if double_set in nums:
                new_int+=nums[double_set]
                i+=2
            else:
                new_int+=nums[v]
                i+=1
        print(new_int)
        return new_int

    # leetcode solution
    def romanToIntElegant(self,s: str) -> int:
        total = nums.get(s[-1])
        for i in reversed(range(len(s) - 1)):
            if nums[s[i]] < nums[s[i + 1]]:
                total -= nums[s[i]]
            else:
                total += nums[s[i]]
        print(total)
        return total