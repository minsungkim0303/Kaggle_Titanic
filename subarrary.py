def maxSubArraySum(a,n):
  
  max_so_far = a[0]
  curr_max = a[0]
  
  for i in range(1,n):
    curr_max = max(a[i], curr_max + a[i])
    max_so_far = max(max_so_far, curr_max)
  return max_so_far

# fuction to check the above fuction
# a = [4, -2, -1, 1, 5] 
# a = [ -2, 1, -3, 4, -1, 2, 1, -5, 4]
#a = [-7, 4, -3, 6, 3, -8, 3, 4]
a = [1, -2, 3, 4]
print"Maximum contiguous sum is" , maxSubArraySum(a,len(a)) 