class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        lp, rp = 0, len(numbers) - 1

        while lp < rp:
            total_sum = numbers[lp] + numbers[rp]

            if total_sum < target:
                lp += 1
            elif total_sum > target:
                rp -= 1
            else:
                return [lp + 1, rp + 1 ]