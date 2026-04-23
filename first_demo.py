print("第一次尝试github拉取填写代码")
nums=[2,5,4,2,3,9,5]
if not nums:
    print(0)
elif len(nums)==1:
    print(nums[0])
else:
    a,b= nums[0],max(nums[0],nums[1])
    for i in range(2,len(nums)):
        c=max(nums[i-1],nums[i-2]+a)
        a,b=b,c
    print(c)