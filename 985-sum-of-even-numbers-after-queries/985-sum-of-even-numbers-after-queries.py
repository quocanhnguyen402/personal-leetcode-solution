class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        leng = len(nums)
        even_sum = 0
        even_index = {}

        for i in range(leng):
            if nums[i] % 2 == 0:
                even_sum += nums[i]
                even_index[i] = True
            else:
                even_index[i] = False

        _result = []
        for i in range(len(queries)):
            index = queries[i][1]
            val = queries[i][0]
            _sum = val + nums[index]
            if _sum % 2 == 0:
                if even_index[index]:
                    even_sum += val
                else:
                    even_index[index] = True
                    even_sum += _sum
            else:
                if even_index[index]:
                    even_index[index] = False
                    even_sum -= nums[index]
            _result.append(even_sum)        
            nums[index] = _sum
        return _result