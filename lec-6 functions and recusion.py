cities =["delhi","gugaoun","dhaka"]

def print_len(list):
    print(len(list))

def print_list(list):
    for el in list:
        print(el, end=" ")
def cal_dact(n):
    fact=1
    for i in range(1,n+1):
        fact *= i
    print(fact)
    
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =",inr_val,"INR")

def number(n):
    if (n % 2==0):
      print("Even") 
    else:
      print("ODD")
#recursion
def fact(n):
    if(n == 1 or n == 0):
        return 1
    return n * fact(n-1)
#exercise
def calc_sum(n):
    if( n == 0):
        return 0
    return n + calc_sum(n-1)

def print_lis(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_lis(list, idx+1)

fruit =["mango","banana","lichi"]
print_lis(fruit)