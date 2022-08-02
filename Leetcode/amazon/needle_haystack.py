def strStr(haystack, needle):
        
        window = len(needle)
        for i in range(0, len(haystack)- window + 1):
            if needle == haystack[i:i+window]:
                return i
        return -1