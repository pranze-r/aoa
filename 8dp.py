#1----Rod Cutting-------
def rod_cutting(prices, n):

    # dp[i] stores maximum profit for rod length i
    dp = [0] * (n + 1)

    for i in range(1, n + 1):

        max_val = -1

        # Try every possible first cut
        for j in range(1, i + 1):

            max_val = max(
                max_val,
                prices[j - 1] + dp[i - j]
            )

        dp[i] = max_val

    return dp[n]


prices = [1, 5, 8, 9]
rod_length = 4

print("Maximum Profit:", rod_cutting(prices, rod_length))




#2------Matrix Chain Multiplication----


def matrix_chain_order(p):

    n = len(p) - 1

    
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    
    for L in range(2, n + 1):

        for i in range(1, n - L + 2):

            j = i + L - 1

            dp[i][j] = float('inf')

            # Try every possible split
            for k in range(i, j):

                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + p[i - 1] * p[k] * p[j]
                )

                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[1][n]


dimensions = [10, 30, 5, 60]

print(
    "Minimum Multiplication Operations:",
    matrix_chain_order(dimensions)
)


#3------Longest Common Subsequence (LCS)----------


def longest_common_subsequence(text1, text2):

    m = len(text1)
    n = len(text2)

    
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    
    for i in range(1, m + 1):

        for j in range(1, n + 1):

            if text1[i - 1] == text2[j - 1]:

                dp[i][j] = 1 + dp[i - 1][j - 1]

            else:

                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

    
    lcs_chars = []

    i = m
    j = n

    while i > 0 and j > 0:

        if text1[i - 1] == text2[j - 1]:

            lcs_chars.append(text1[i - 1])

            i -= 1
            j -= 1

        elif dp[i - 1][j] > dp[i][j - 1]:

            i -= 1

        else:

            j -= 1

    lcs_str = "".join(reversed(lcs_chars))

    return dp[m][n], lcs_str


seq1 = "BATMAN"
seq2 = "CATWOMAN"

length, sequence = longest_common_subsequence(seq1, seq2)

print("LCS Length:", length)
print("Subsequence:", sequence)
