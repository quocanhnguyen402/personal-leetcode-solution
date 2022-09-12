class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        begin, end = 0, len(tokens) - 1
        score = 0
        max_score = score
        while begin <= end:
            if tokens[begin] <= power:
                power -= tokens[begin]
                score += 1
                max_score = max(max_score, score)
                begin += 1
            elif score > 0:
                power += tokens[end]
                score -= 1
                max_score = max(max_score, score)
                end -= 1
            else:
                break
        return max_score
        