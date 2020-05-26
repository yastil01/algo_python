def quicksort(nums):
    if len(nums) <= 1:
        return nums

    pivot = nums[0]
    lt = [v for v in nums if v < pivot]
    eq = [v for v in nums if v == pivot]
    gt = [v for v in nums if v > pivot]

    return quicksort(lt) + eq + quicksort(gt)

nums = [3,4,2,1]
print(quicksort(nums))
