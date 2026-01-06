# prices = [50,20,"20", 120,30,80]
# total = 0
# for price in prices:
#     total += int(price)
# print(total)


# marks = [35, 78, 42, 20, 90,50,60,70]
# count = 0
# for mark in marks:
#     if mark >= 40:
#         count += 1

# print("student passed: ",count)

""" ============= find the highest salary==============="""
# salaries = [15000, 22000, 18000, 30000]
# height = salaries[0]
# for salary in salaries:
#     if salary >height:
#         height = salary
# print(height)

# print(max(salaries))

""" ============= removed 0 values ==============="""

# stock = [10, 0, 5, 0, 8]
# new_stock = []

# for item in stock:
#     if item == 0:
#         continue
#     else:
#         new_stock.append(item)
# print(new_stock)

""" ============= avg temperature ==============="""

# temps = [30, 32, 31, 29, 33]
# print(sum(temps)/len(temps))

""" ============= convert reverse list ==============="""
# messages = ["hi", "how are you", "bye"]
# print(messages[::-1])
# messages.reverse()
# print(messages)

""" ============= find dublicate number  ==============="""
# numbers = [1, 2, 3, 2, 4, 1]
# dublicated = []
# for num in numbers:
#     if num not in dublicated and numbers.count(num)>1:
#         dublicated.append(num)

# print(dublicated)

def my_decorator(func):
    def wrapper():
        return func()
    return wrapper

