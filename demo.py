print("hello")
print("trying for the first time")


def sort(nums):
    for i in range(len(nums) - 1):
        minPosition = i

        for j in range(i, len(nums)):
            if nums[j] < nums[minPosition]:
                minPosition = j

        temp = nums[i]
        nums[i] = nums[minPosition]
        nums[minPosition] = temp


nums = [3, 6, 8, 3, 4, 6, 0]
sort(nums)

print(nums)