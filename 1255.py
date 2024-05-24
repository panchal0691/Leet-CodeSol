class Solution:
    def __init__(self):
        self.n = 0
        self.maxScore = float('-inf')

    def solve(self, i, score, words, currScore, freq):
        self.maxScore = max(self.maxScore, currScore)

        if i >= self.n:
            return

        tempFreq = freq[:]

        j = 0
        tempScore = 0

        while j < len(words[i]):
            ch = words[i][j]

            tempFreq[ord(ch) - ord('a')] -= 1
            tempScore += score[ord(ch) - ord('a')]

            if tempFreq[ord(ch) - ord('a')] < 0:
                break

            j += 1

        # Take words[i]
        if j == len(words[i]):  # It means we could form the word words[i]
            self.solve(i + 1, score, words, currScore + tempScore, tempFreq)

        # Not Take words[i]
        self.solve(i + 1, score, words, currScore, freq)

    def maxScoreWords(self, words, letters, score):
        freq = [0] * 26

        for ch in letters:
            freq[ord(ch) - ord('a')] += 1

        self.n = len(words)

        self.solve(0, score, words, 0, freq)

        return self.maxScore
