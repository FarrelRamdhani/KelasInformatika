#Compute GCD
def compute_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

#Compute LCM
def compute_lcm(x, y):
    lcm = (x*y)//compute_gcd(x, y)
    return lcm

num1 = 12
num2 = 20

print("Nilai L.C.M adalah", compute_lcm(num1, num2))
