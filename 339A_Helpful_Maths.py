nums = list(input().split("+"))
sorted_nums = sorted(nums)
output_str = []
for i in range(len(sorted_nums)-1):
    output_str.append(sorted_nums[i] + "+")
output_str.append(sorted_nums[len(sorted_nums)-1])
output_str = "".join(output_str)
print(output_str)