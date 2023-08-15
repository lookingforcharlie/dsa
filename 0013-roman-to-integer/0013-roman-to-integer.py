class Solution:
    def romanToInt(self, s: str) -> int:
        convertChart = {'I':  1, 'V':  5, 'X': 10,
                        'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        intResult = 0

        index = 0
        while index < len(s):
            if index < len(s) - 1 and convertChart[s[index]] < convertChart[s[index + 1]]:
                intResult += convertChart[s[index + 1]
                                          ] - convertChart[s[index]]
                index += 2  # Skip the next character
            else:
                intResult += convertChart[s[index]]
                index += 1

        return intResult