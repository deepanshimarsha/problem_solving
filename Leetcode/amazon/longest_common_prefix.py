def LongestCommonPrefix(strs):
    strs = sorted(strs)
    prefix = strs[0]
    for i in range(1,len(strs)):
        n = len(prefix)
        if strs[i][0:n] == prefix:
            continue
        else:
            while n > 0:
                n = n - 1
                prefix = prefix[0:n]
                if strs[i][0:n] == prefix:
                    break
            if n == 0:
                return ""
    return prefix

print(LongestCommonPrefix( ["dog","racecar","car"]))

