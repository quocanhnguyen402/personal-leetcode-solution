class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {
            1 : "I",
            4 : "IV",
            5 : "V",
            9 : "IX",
            10 : "X",
            40 : "XL",
            50 : "L",
            90 : "XC",
            100 : "C",
            400 : "CD",
            500 : "D",
            900 : "CM",
            1000 : "M"
        }

        nums = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        
        res = ""
        a = len(nums) - 1
        
        while num != 0:
            while nums[a] > num:
                a -= 1
            num -= nums[a]
            res += roman[nums[a]]
        return res    