username = input()
num_distinct_letters = len(set(username))
print("CHAT WITH HER!" if num_distinct_letters % 2 ==0 else "IGNORE HIM!")