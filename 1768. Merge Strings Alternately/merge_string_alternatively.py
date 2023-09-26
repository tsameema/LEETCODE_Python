
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not (1 <= len(word1) <= 100) or not (1 <= len(word2) <= 100):
            return 'Length of words is not within the specified range'

        min_len = min(len(word1), len(word2))
        result = ''.join(word1[i] + word2[i] for i in range(min_len))
        result += (word1[min_len:] + word2[min_len:])
        return result

if __name__ == "__main__":
    s = Solution()
    word1, word2 = "abcd", "pq"
    alternate_words = s.mergeAlternately(word1, word2)
    print(alternate_words)

