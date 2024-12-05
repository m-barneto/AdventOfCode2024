left: list[int] = []
right: list[int] = []

with open("p1.txt") as input:
    for line in input:
        nums = line.split("   ")
        left.append(int(nums[0]))
        right.append(int(nums[1]))


left.sort()
right.sort()

distance: int = 0

for i in range(len(left)):
    distance += abs(left[i] - right[i])

print(distance)
