n=int(input("Enter the amount of fibonacci numbers you want to be displayed: "))
fib_list = [0, 1]
while len(fib_list) < n:
    fib_list.append(fib_list[-1] + fib_list[-2])
print(fib_list)