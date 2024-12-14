import sys

def equal_min_moves(nums):
    nums.sort()
    med = nums[len(nums) // 2]
    return sum(abs(num - med) for num in nums)

if __name__ == "__main__":
    file_path = sys.argv[1]
    with open(file_path, 'r') as file:
        nums = [int(line.strip()) for line in file if line.strip().isdigit()]

    res = equal_min_moves(nums)
    print(res)
