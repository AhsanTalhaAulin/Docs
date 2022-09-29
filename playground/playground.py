
# nums =[1,2,3,4]
# runningSum = []


# runningSum.append(nums[0])

# for i in range (1, len(nums)):
#     print(nums[i], runningSum[i-1])
#     runningSum.append(nums[i]+runningSum[i-1])

# print(runningSum)

# def solve(nums, k):
#    dictionary={}
#    for num in nums:
#       if num not in dictionary:
#          dictionary[num]=1
#       else:
#          dictionary[num]+=1
#    count=len(dictionary)
#    for frequency in sorted(dictionary.values()):
#       k-=frequency
#       if(k<0):
#          return count
#       else:
#          count-=1
#    return count
# nums = [5,4,2,2,4,4,3,3,3,3]
# k = 3
# print(solve(nums, k))


# def cumulative_nums(nums):
#    cumulative_nums = []
#    cumulative_nums.append(nums[0])
#    for index in range (1, len(nums)):
#       cumulative_nums.append(nums[index]+cumulative_nums[index-1])
#    return cumulative_nums

# def reverse_cumulative_nums(nums):
#    reverse_cumulative_nums = [len(nums)]
#    reverse_cumulative_nums[len(nums)-1] = nums[len(nums)-1]

#    for index in range (len(nums)-2, -1, -1):
#       reverse_cumulative_nums[index] = nums[index]+reverse_cumulative_nums[index+1]
#    return reverse_cumulative_nums


# nums = [1,7,3,6,5,6]
# nums = [1,2,3]
# nums = [-1,-1,-1,-1,-1,0]

# pivot_index = -1

# sum_nums = sum(nums)

# cumilitive_sum = 0

# for index, nums in enumerate(nums):
#    print("index: ", index, "nums: ", nums, "cumilitive_sum: ", cumilitive_sum, "Sum - cumilitive sum: ", sum_nums- cumilitive_sum-nums)
#    if(cumilitive_sum == sum_nums- cumilitive_sum - nums):
#       pivot_index = index
#       break
#    cumilitive_sum += nums


# print(pivot_index)


# string1 = 'paperee'
# string2 = 'titleee'

# if  not (len(string1) == len(string2)):
#    print('false')

# dict1 = {}
# dict2 = {}

# for char in string1:
#    if char not in dict1:
#       dict1[char] = 1
#    else:
#       dict1[char] += 1

# for char in string2:
#    if char not in dict2:
#       dict2[char] = 1
#    else:
#       dict2[char] += 1

# print(dict1)
# print(dict2)

# dict1 = dict(sorted(dict1.items(),key=lambda item:item[1]))
# dict2 = dict(sorted(dict2.items(),key=lambda item:item[1]))


# print(dict1)
# print(dict2)


# for value1, value2 in zip(dict1.values(), dict2.values()):
#    if value1 != value2:
#       print('false')
#       break

# print('true')


# ar1 = dict1.values()
# print(ar1)


def make_dict(string):
      dictionary = {}
      for char in string:
         if char not in dictionary:
            dictionary[char] = 1
         else:
            dictionary[char] += 1
      return dictionary


def solution(s, t):

      if (len(s)!=len(t)):
         return False
      dict1 = {}
      dict2 = {}

      for char in s:
         if char not in dict1:
            dict1[char] = 1
         else:
            dict1[char] += 1
      for char in t:
         if char not in dict2:
            dict2[char] = 1
         else:
            dict2[char] += 1

      print(dict1)
      print(dict2)
      
      list1 = list(dict1.values())
      list2 = list(dict2.values())


      print(list1, list2)
      list1.sort()
      list2.sort()
      print(list1, list2)

      if (list1 != list2):
         return False
      return True


print(solution("bbbaaaba", "aaabbbba"))

