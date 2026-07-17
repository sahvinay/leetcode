class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        no_deletion = arr[0]
        one_deletion = float('-inf')
        result = arr[0]

        for i in arr[1:]:
            prev_no_deletion = no_deletion
            prev_one_deletion = one_deletion
            no_deletion = max(prev_no_deletion + i, i)
            one_deletion = max(prev_one_deletion + i, prev_no_deletion)
            result = max(result, no_deletion, one_deletion)
        return result