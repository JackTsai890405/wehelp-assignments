# -*- coding:utf-8 -*-

# 第一題
from typing import Counter


def calculate(min, max):
    sum = 0
    for x in range(min, max+1): 
        sum = sum + x
    print(sum) 

calculate(1, 3)
calculate(4, 8)

# 第二題
def avg(data):
    totalPeople = 0 # 總人數
    totalSalary = 0 # 總薪資
    average = 0 # 平均薪水
    for x in data:
        if x == "count": 
            totalPeople = data[x]
        else:
            for y in data[x]:
                totalSalary += y["salary"]
    average = totalSalary/totalPeople
    print(average)

avg({ # Tuple --> Dictionary --> List --> Dictionary
    "count":3, 
    "employees":[
        {
            "name":"John",
            "salary":30000 
        },
        {
            "name":"Bob",
            "salary":60000 
        },
        {
            "name":"Jenny",
            "salary":50000 
        }
    ]
})

# 第三題
def maxProduct(nums):
    if len(nums) == 2:
        max = nums[0] * nums[1]
        print(max)
    else:
        max = 0
        for x in range(len(nums)): 
            for y in range(len(nums)):
                if(nums[x] != nums[y]):
                    if max < nums[x] * nums[y]:
                        max = nums[x] * nums[y]
        print(max)
        
maxProduct([5, 20, 2, 6]) # 得到 120 
maxProduct([10, -20, 0, 3]) # 得到 30 
maxProduct([-1, 2]) # 得到 -2 
maxProduct([-1, 0, 2]) # 得到 0

# 第四題
def twoSum(nums, target):
    finalAnswer = []
    for numA in range(len(nums)): 
        for numB in range(len(nums)):
            if nums[numA] != nums[numB]: 
                if nums[numA] + nums[numB] == target:
                    finalAnswer.append(numA)
    return finalAnswer
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

# 第五題
def maxZeros(nums):
    count = 0
    maxCount = 0
    for num in nums:
        if num == 0:
            count = count + 1
            if count > maxCount:
                maxCount = count
        elif num != 0: 
            count = 0
    print(maxCount)
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4 
maxZeros([1, 1, 1, 1, 1]) # 得到 0 
maxZeros([0, 0, 0, 1, 1]) # 得到 3