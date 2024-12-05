left: list[int] = []
right: list[int] = []

with open("input.txt") as input:
    for line in input:
        nums = line.split("   ")
        left.append(int(nums[0]))
        right.append(int(nums[1]))

similarity: int = 0

for i in range(len(left)):
    num = left[i]
    count = right.count(num)
    similarity += num * count

print("Similarity:", similarity)

