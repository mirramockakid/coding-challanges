import re

path = "./day2_input.txt"
days_file = open(path,'r')
success_1 = 0
success_2 = 0

for line in days_file:
    o = re.split('\s+', line)
    min_max = re.findall(r'\d+', o[0])
    char = re.findall(r'\w', o[1])
    
    ret_1 = password_policy_1(
        min = int(min_max[0]), 
        max = int(min_max[1]), 
        char = char[0], 
        password = o[2])
    
    ret_2 = password_policy_2(
        min = int(min_max[0]), 
        max = int(min_max[1]), 
        char = char[0], 
        password = o[2])
    
    if ret_1 != 0:
        success_1 += 1
    
    if ret_2 != 0:
        success_2 += 1

print("Number of correct passwords based on policy #1: ", success_1)
print("Number of correct passwords based on policy #2: ", success_2)

days_file.close

def password_policy_1(min, max, char, password):
    n = int(password.count(char))
    if n >= min and n <= max:
        return 1
    else:
        return 0

def password_policy_2(min, max, char, password):
    if (password[min-1] == char) is not (password[max-1] == char):
        return 1
    else:
        return 0


