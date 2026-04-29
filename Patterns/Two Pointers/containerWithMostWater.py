class Solution(object):
    def __init__(self, height):
        self.height = height

    def maxArea(self):
        height = self.height
        left = 0
        right = len(height) - 1
        mx_area = 0

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            area = width * current_height

            mx_area = max(mx_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return mx_area


# Example usage
if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    obj = Solution(height)
    result = obj.maxArea()
    print("Maximum water that can be contained:", result)