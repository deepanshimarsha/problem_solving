def roman_to_integer(s):
    dic = {"j":0,"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    digit = 0
    prev = "j"
    for ele in s[::-1]:
        if dic[prev] > dic[ele]:
            digit -= dic[ele]
        else:
            digit += dic[ele]
        prev = ele
    return digit

print(roman_to_integer("LVIII"))
