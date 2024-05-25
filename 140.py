class Solution:
    def __init__(self):
        self.result = []
        self.dict = set()

    def solve(self, i, curr_sentence, s):
        if i >= len(s):
            self.result.append(curr_sentence.strip())
            return

        for j in range(i, len(s)):
            temp_word = s[i:j+1]

            if temp_word in self.dict:
                orig_sentence = curr_sentence
                if curr_sentence:
                    curr_sentence += " "
                curr_sentence += temp_word

                self.solve(j+1, curr_sentence, s)

                curr_sentence = orig_sentence

    def wordBreak(self, s, wordDict):
        self.dict = set(wordDict)
        curr_sentence = ""
        self.solve(0, curr_sentence, s)
        return self.result
