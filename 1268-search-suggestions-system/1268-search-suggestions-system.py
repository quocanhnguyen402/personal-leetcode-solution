class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        search_len = len(searchWord)
        left = 0
        right = len(products) - 1
        res = []
        for i in range(search_len):
            char = searchWord[i]
            while left <= right and (len(products[left]) <= i or products[left][i] != char):
                left += 1
            while left <= right and (len(products[right]) <= i or products[right][i] != char):
                right -= 1
            res.append([])
            remain = min(3,right - left + 1)
            for a in range(remain):
                res[-1].append(products[left + a])
        return res
            