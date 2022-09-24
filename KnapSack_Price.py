# Find Profit by Price
def profitByWeight(Price_Weight: list, KnapSack: int) -> int:

    Profit = 0

    for P_W in Price_Weight:

        if KnapSack <= 0:
            break

        if P_W[0] <= KnapSack:
            Profit += P_W[1]
            KnapSack -= P_W[0]
        else:
            Profit += (KnapSack/P_W[0])*P_W[1]
            KnapSack -= P_W[0]

    return Profit


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

    # Make pair of Price and Weight
    Price_Weight = []
    for P_W in zip(Price, Weight):
        Price_Weight.append(P_W)

    # Sort pair in descending order by Price
    Price_Weight.sort(reverse=True)

    print("Output :")
    # Print Profit
    print(profitByWeight(Price_Weight, KnapSack))


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