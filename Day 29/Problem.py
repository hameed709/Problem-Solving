def numFrequency(nums, k):
    nums.sort()

    left = 0
    window_sum = 0
    max_freq = 1

    for right in range(len(nums)):
        window_sum += nums[right]
        cost = nums[right] * (right - left + 1) - window_sum
        while cost > k:
            window_sum -= nums[left]
            left += 1
            cost = nums[right] * (right - left + 1) - window_sum
        max_freq = max(max_freq, right - left + 1)
    return max_freq