# def subarray_sort_range(nums):

#     if all(nums[i] <= nums[i+1] for i in range(len(nums)-1)):
#         return (-1, -1)
    
#     left = 0
#     while left < len(nums) - 1 and nums[left] <= nums[left + 1]:
#         left += 1

#     right = len(nums) - 1
#     while right > 0 and nums[right] >= nums[right - 1]:
#         right -= 1

#     def min_arr(arr):
#         min_num = 0
#         for i in range(len(arr)-1):
#             if arr[i] < arr[i+1]:
#                 min_num = arr[i]
#             i+=1
#         return(min_num)
    
#     def max_arr(arr):
#         max_num = 0
#         for i in range(len(arr)-1):
#             if arr[i] > arr[i+1]:
#                 max_num = arr[i]
#             i+=1
#         return(max_num)

#     sub_min = min_arr(nums[left:right+1])
#     sub_max = max_arr(nums[left:right+1])
#     while left > 0 and nums[left - 1] > sub_min:
#         left -= 1
#     while right < len(nums) - 1 and nums[right + 1] < sub_max:
#         right += 1

#     return (left, right)


def find_unsorted_subarray(nums):
    n = len(nums)

    left = 0
    while left < n - 1 and nums[left] <= nums[left + 1]:
        left += 1
    if left == n - 1:  
        return None


    right = n - 1
    while right > 0 and nums[right] >= nums[right - 1]:
        right -= 1


    sub_min = min(nums[left:right+1])
    sub_max = max(nums[left:right+1])


    while left > 0 and nums[left - 1] > sub_min:
        left -= 1
    while right < n - 1 and nums[right + 1] < sub_max:
        right += 1

    bounds = (left, right)
    if bounds is None:
        return (None, nums)

    start, end = bounds
    del nums[start+1:end+1]
    return nums



if __name__ == "__main__":
    text = input("ведіть масив у виді 1,2,3,4,...   :")
    arr_text = text.split(",")
    arr = []

    for i in arr_text:
        arr.append(int(i))
    result = find_unsorted_subarray(arr)
    print(result)
