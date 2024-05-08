class Solution:
    def findRelativeRanks(self, score):
        n = len(score)
        result = [None] * n
        mp = {}

        for i in range(n):
            mp[score[i]] = i  # ith athlete

        score.sort(reverse=True)  # descending

        for i in range(n):
            if i == 0:  # 1st Rank athlete
                ath = mp[score[i]]
                result[ath] = "Gold Medal"
            elif i == 1:
                ath = mp[score[i]]
                result[ath] = "Silver Medal"
            elif i == 2:
                ath = mp[score[i]]
                result[ath] = "Bronze Medal"
            else:
                ath = mp[score[i]]
                result[ath] = str(i + 1)

        return result
