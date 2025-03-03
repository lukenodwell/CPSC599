N, W = map(int, input().split())

weeks_data = [None] * (W + 1)
for w in range(W + 1):
    line = list(map(int, input().split()))
    K = line[0]
    prices = line[1 : K + 1]
    sales = line[K + 1 : 2 * K + 1]
    weeks_data[W - w] = (K, prices, sales)

dp = [[0 for _ in range(N + 1)] for _ in range(W + 1)]

choices = [[float('inf') for _ in range(N + 1)] for _ in range(W + 1)]

K0, prices0, sales0 = weeks_data[0]
for n in range(N + 1):
    best_revenue = 0
    best_price = float('inf')
    for i in range(K0):
        tickets_sold = min(n, sales0[i])
        revenue = tickets_sold * prices0[i]
        if revenue > best_revenue or (revenue == best_revenue and prices0[i] < best_price):
            best_revenue = revenue
            best_price = prices0[i]
    dp[0][n] = best_revenue
    choices[0][n] = best_price

for w in range(1, W + 1):
    K, prices, sales = weeks_data[w]
    for n in range(N + 1):
        best_revenue = 0
        best_price = float('inf')
        for i in range(K):
            tickets_sold = min(n, sales[i])
            current_revenue = tickets_sold * prices[i]
            
            remaining_seats = n - tickets_sold
            
            total_revenue = current_revenue + dp[w - 1][remaining_seats]
            
            if total_revenue > best_revenue or (total_revenue == best_revenue and prices[i] < best_price):
                best_revenue = total_revenue
                best_price = prices[i]
        
        dp[w][n] = best_revenue
        choices[w][n] = best_price

max_rev = dp[W][N]

price_week_W = choices[W][N]

print(max_rev)
print(price_week_W)