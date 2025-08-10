class TwoPointer:

    # Opposite Ends - Sum Search / Palindrome Check / Two Sum Sorted
    def opposite_ends(self, arr, target):
        left, right = 0, len(arr) - 1
        while left < right:
            curr_sum = arr[left] + arr[right]
            if curr_sum == target:
                return [left, right]  # or True/False for palindrome
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
        return None

    # Same Direction - Slow/Fast Pointer (Cycle Detection / Middle Node)
    def slow_fast(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # cycle detected
                return True
        return False

    # Sliding Window - Fixed Size
    def fixed_window(self, arr, k):
        left = 0
        curr_sum = 0
        max_sum = float('-inf')
        for right in range(len(arr)):
            curr_sum += arr[right]
            if right - left + 1 == k:  # window reached size
                max_sum = max(max_sum, curr_sum)
                curr_sum -= arr[left]
                left += 1
        return max_sum

    # Sliding Window - Variable Size (smallest subarray sum >= target)
    def variable_window(self, arr, target):
        left = 0
        curr_sum = 0
        min_len = float('inf')
        for right in range(len(arr)):
            curr_sum += arr[right]
            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= arr[left]
                left += 1
        return 0 if min_len == float('inf') else min_len

    # Partition / Dutch National Flag (Sort Colors / Move Zeroes)
    def partition(self, arr):
        left, right = 0, len(arr) - 1
        i = 0
        while i <= right:
            if arr[i] == 0:
                arr[i], arr[left] = arr[left], arr[i]
                left += 1
                i += 1
            elif arr[i] == 2:
                arr[i], arr[right] = arr[right], arr[i]
                right -= 1
            else:
                i += 1
        return arr


# Example Usage
tp = TwoPointer()
print(tp.opposite_ends([1, 2, 3, 4, 6], 6))          # Two sum sorted
print(tp.fixed_window([1, 2, 3, 4, 5], 3))           # Max sum in fixed window
print(tp.variable_window([2, 1, 5, 2, 3, 2], 7))     # Min subarray length
print(tp.partition([2, 0, 2, 1, 1, 0]))              # Dutch National Flag

