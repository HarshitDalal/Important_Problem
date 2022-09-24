N_R = {
    10000: 'H', 9000: 'MH', 5000: 'G', 4000: 'MG',
    1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
    100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
    10: 'X', 9: 'IX', 5: 'V', 4: 'IV',
    1: 'I'    
}
def printRoman(num):
    res = ""
    for cap, roman in N_R.items():
        d, m = divmod(num, cap)
        res += roman * d
        num = m
    return res


# Driver code
if __name__ == "__main__":
    number = int(input())
    print("Roman value is:", printRoman(number))

    

