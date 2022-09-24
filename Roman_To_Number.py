R_N = {
    'H': 10000, 'MH': 9000, 'G': 5000, 'MG': 4000,
    'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
    'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
    'X': 10, 'IX': 9, 'V': 5, 'IV': 4,
    'I': 1
}
def printNumber(rom):
    i = 0
    num = 0
    l = len(rom)
    while i < l:
        if i+1 < l and rom[i:i+2] in R_N:
            num += R_N[rom[i:i+2]]
            i += 2
        else:
            num += R_N[rom[i]]
            i += 1
    return num

# Driver code
if __name__ == "__main__":
    roman = input().upper()
    print('Number value is:', printNumber(roman))