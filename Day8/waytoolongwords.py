class Solution:
    def longwords(self, str_list):
        print(f"Initial list of words: {str_list}")
        
        for word in str_list:
            length=len(word)
            if length > 10:
                final= f"{word[:1]}{length-2}{word[-1:]}"
                print(final)
            else:
                print(word)

sol= Solution()

# --- Test Cases ---
sol.longwords(["short", "tiny", "longerword", "pneumonoultramicroscopicsilicovolcanoconiosis"])

