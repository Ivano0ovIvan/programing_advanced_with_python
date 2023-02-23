from collections import deque


bowls_of_ramen = deque([int(x) for x in input().split(', ')])
customers = deque([int(x) for x in input().split(', ')])

while customers:
    if not bowls_of_ramen:
        print("Out of ramen! You didn't manage to serve all customers.")
        print(f"Customers left: {', '.join(map(str, customers))}")
        break

    customer = customers.popleft()
    bowl = bowls_of_ramen.pop()

    if customer > bowl:
        customers.appendleft(customer - bowl)
    elif customer < bowl:
        bowls_of_ramen.append(bowl - customer)

else:
    print(f"Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join(map(str,bowls_of_ramen))}")