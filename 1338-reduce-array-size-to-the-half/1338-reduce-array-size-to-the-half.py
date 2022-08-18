class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr_len = len(arr) // 2
        left = 0
        right = arr_len*2 - 1
        map = {}
        while left < right:
            if arr[left] not in map:
                map[arr[left]] = 1
            else:
                map[arr[left]] += 1
            
            if arr[right] not in map:
                map[arr[right]] = 1
            else:
                map[arr[right]] += 1
            left += 1
            right -= 1
        result = []
        
        for key in map:
            result.append(map[key])
        result.sort(reverse=True)

        sum = 0
        count = 0
        for i in range(0,len(result)):
            sum += result[i]
            count += 1
            if sum >= arr_len:
                return count