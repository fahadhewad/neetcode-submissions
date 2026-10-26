class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            length_word = len(word)
            encoded = encoded + str(length_word) + ";" + word
        
        print(encoded)
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != ";":
                j += 1
            length_word = int(s[i:j])
            i = j + 1
            decoded.append(s[i:i + length_word])
            i += length_word
        return decoded