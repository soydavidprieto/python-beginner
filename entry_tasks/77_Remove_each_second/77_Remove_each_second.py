if __name__ == '__main__':
    nums = input("Please enter  sequence of numbers : ").split(',')    #Example: 3,2,1,4,11,5,2
    del nums[1::2]
    for i in range(len(nums)):
        nums[i] = str.strip((nums[i]))
    nums1 = nums[::-1]
    print(nums1)

