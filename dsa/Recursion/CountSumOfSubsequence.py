class Solution:

    def perfectSum(self, arr, target):

        result = []
        count = 0

        def solve(index, curr_sum, subset):

            nonlocal count

            if index >= len(arr):

                if curr_sum == target:
                    result.append(subset.copy())
                    count += 1

                return

            subset.append(arr[index])

            solve(
                index + 1,
                curr_sum + arr[index],
                subset
            )

            subset.pop()

            solve(
                index + 1,
                curr_sum,
                subset
            )

        solve(0, 0, [])

        return count