# Find Profit by Weight
def profitByWeight(Weight_Price: list, KnapSack: int) -> int:

    Profit = 0

    for W_P in Weight_Price:

        if KnapSack <= 0:
            break

        if W_P[0] <= KnapSack:
            Profit += W_P[1]
            KnapSack -= W_P[0]
        else:
            Profit += (KnapSack/W_P[0])*W_P[1]
            KnapSack -= W_P[0]

    return round(Profit, 2)


def main() -> None:
    # Size of array
    N = int(input())

    # Weight of products
    Weight = []
    for _ in range(N):
        Weight.append(int(input()))

    # Price of products
    Price = []
    for _ in range(N):
        Price.append(int(input()))

    # Capacity of KnapSack
    KnapSack = int(input())

    # Make pair of Weight and Price
    Weight_Price = []
    for W_P in zip(Weight, Price):
        Weight_Price.append(W_P)

    # Sort pair in ascending order by Weight
    Weight_Price.sort()

    print("Output :")
    # Print Profit
    print(profitByWeight(Weight_Price, KnapSack))


if __name__ == '__main__':
    main()


# N : 3
# W1 : 20
# W2 : 30
# W3 : 10
# P1 : 100
# P2 : 120
# P3 : 60
# KS : 50

# Output = 240.0

# N : 3
# W1 : 18
# W2 : 15
# W3 : 10
# P1 : 25
# P2 : 24
# P3 : 15
# KS : 20


# Output = 31.0
