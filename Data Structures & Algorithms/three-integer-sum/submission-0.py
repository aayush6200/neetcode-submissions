class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ## we can use the set to store the resule, so that it maintains uniqueness.. else we can also use the loop so that the one of three elem are unique

        ## first lets solve by using the set method..
        result = set()
        nums.sort()
        for i in range(len(nums) - 2):
            lp = i + 1          # left pointer inside the loop
            rp = len(nums) - 1  # right pointer inside the loop
            target = -(nums[i])
            while lp < rp:
                if nums[lp] + nums[rp] == target:
                    result.add((nums[i], nums[lp], nums[rp]))
                    lp += 1
                    rp -= 1
                elif nums[lp] + nums[rp] > target:
                    rp -= 1
                else:
                    lp += 1
        return list(result)

            