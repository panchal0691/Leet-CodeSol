class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = [[]]
        used = [0]

        for word in words:
            if used[-1] ==0:
                lines[-1].append(word)
                used[-1] += len(word)

            elif used[-1] + len(word) +1 <= maxWidth:
                lines[-1].append(word)
                used[-1] += len(word) +1
            else:
                lines.append([word])
                used.append(len(word))

        ans = []

        for line, cused in zip(lines[:-1],used):
            gaps = len(line) -1
            extra_spaces = maxWidth - cused

            if gaps ==0:
                current = line[0]
                spaces = maxWidth - len(line[0])
                ans.append(current + " "* spaces)
                continue

            each_spaces = extra_spaces // gaps +1
            leftovers = extra_spaces % gaps

            current_line = [line[0]]


            for word in line[1:]:
                current_line.append(" "* (each_spaces))

                if leftovers >0:
                    current_line.append(" ")
                    leftovers -=1
                current_line.append(word)


            ans.append("".join(current_line))




        last_line = " ".join(lines[-1])
        spaces = maxWidth - len(last_line)

        ans.append(last_line + " "* spaces)
        return ans
