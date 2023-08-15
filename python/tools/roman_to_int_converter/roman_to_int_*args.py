#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#largest to smallest: add them up
#smaller before larger: subtract smaller

class Solution:
    #*args to process many numerals
    def romanToInt(*s: str) -> int:
        #largest to smallest: add them up
        #smaller before larger: subtract smaller
        roman_nums = { 'I':1, 'V':5, 'X':10, 'L':50, 
        'C':100, 'D':500, 'M':1000}
        
        total = 0
        
        for char in range(len(s)):
            #get roman numeral from tuple
            roman = s[char]
            #get each roman character
            for i in range(len(roman)):
            #decide is to add or subtract
            #if left roman index is smaller subtract
                if i + 1 < len(roman) and roman_nums[roman[i]] < roman_nums[roman[i + 1]]:
                    total -= roman_nums[roman[i]]
                else:
                #if left roman is bigger add     
                    total += roman_nums[roman[i]]
            print(f"{roman}:{total}")
            #set total to zero for next roman numeral
            total = 0
        return 
            
print(Solution.romanToInt("III", "LVIII", "MCMXCIV"))