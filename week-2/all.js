// 第一題
function calculate(min, max) {
    // 請用你的程式補完這個函式的區塊 
    let sum = 0;
    for (min; min <= max; min++) {
        sum += min
    }
    console.log(sum);
}
calculate(1, 3); // 你的程式要能夠計算 1+2+3，最後印出 6 
calculate(4, 8); // 你的程式要能夠計算 4+5+6+7+8，最後印出 30

// 第二題
function avg(data) {
    // 請用你的程式補完這個函式的區塊 
    let sum = 0
    let count = data.count
    data.employees.forEach((item) => {
        sum += item.salary
    });
    console.log(sum / count)
}
avg({
    "count": 3,
    "employees": [
        {
            "name": "John",
            "salary": 30000
        },
        {
            "name": "Bob",
            "salary": 60000
        },
        {
            "name": "Jenny",
            "salary": 50000
        }
    ]
}); // 呼叫 avg 函式

// 第三題
function maxProduct(nums) {
    if (nums.length === 2) {
        console.log(nums[0] * nums[1])
        return
    }

    max = 0
    nums.forEach(function (item, index, array) {
        nums.forEach(function (item2, index2, array2) {
            if (item !== item2) {
                if (max < item * item2) {
                    max = item * item2
                }
            }
        })
    })
    console.log(max)
}
maxProduct([5, 20, 2, 6]) // 得到 120 
maxProduct([10, -20, 0, 3]) // 得到 30 
maxProduct([-1, 2]) // 得到 -2 
maxProduct([-1, 0, 2]) // 得到 0

// 第四題
function twoSum(nums, target) {
    let show = []
    nums.forEach(function (item, index, array) {
        nums.forEach(function (item2, index2, array2) {
            if (item + item2 === target) {
                show.push(index)
            }
        })
    })
    return show
}
let result = twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9

// 第五題
function maxZeros(nums) {
    count = 0
    nums.forEach((item, index, array) => {
        if (index !== array.length - 1) {
            if (item === 0 && array[index+1] === 0) {
                count += 1
            }
        }
    })
    if(nums[0] === 0) {
        console.log(count + 1);
    }
    else {
        console.log(count);
    }
}

maxZeros([0, 1, 0, 0]); // 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4 
maxZeros([1, 1, 1, 1, 1]); // 得到 0 
maxZeros([0, 0, 0, 1, 1]) // 得到 3