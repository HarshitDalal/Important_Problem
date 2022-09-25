# Find Profit by Price
def profitByPriceWeightRatio(Price_Weight_Ratio: list, KnapSack: int) -> int:

    Profit = 0

    for P_W in Price_Weight_Ratio:

        if KnapSack <= 0:
            break

        if P_W[1] <= KnapSack:
            Profit += P_W[0]
            KnapSack -= P_W[1]
        else:
            Profit += (KnapSack/P_W[1])*P_W[0]
            KnapSack -= P_W[0]

    return round(Profit, 2)


def main() -> None:
    # Size of array
    N = int(input())

    # Price of products
    Price = []
    for _ in range(N):
        Price.append(int(input()))

    # Weight of products
    Weight = []
    for _ in range(N):
        Weight.append(int(input()))

    # Capacity of KnapSack
    KnapSack = int(input())

    # Make pair of Price , Weight and Price/Weight
    Price_Weight_Ratio = []
    for P_W in zip(Price, Weight):
        Price_Weight_Ratio.append((P_W[0], P_W[1], round(P_W[0]/P_W[1], 2)))

    # Sort pair in descending order by Price
    Price_Weight_Ratio.sort(key=lambda x: x[2], reverse=True)

    print("Output :")
    # Print Profit
    print(profitByPriceWeightRatio(Price_Weight_Ratio, KnapSack))


if __name__ == '__main__':
    main()

# N : 3
# P1 : 100
# P2 : 120
# P3 : 60
# W1 : 20
# W2 : 30
# W3 : 10
# KS : 50

# Output : 240.0

# N : 3
# P1 : 25
# P2 : 24
# P3 : 15
# W1 : 18
# W2 : 15
# W3 : 10
# KS : 20

# Output : 31.5
