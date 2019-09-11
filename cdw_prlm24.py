'''
Implement the code to check if the given number is a Keith number. 
Return the number number of iteration needed to confirm it; otherwise return false.
'''
n = 197


def is_keith_number(n):
    dg_ls = [int(i) for i in str(n)]
    iteration = 1
    while sum(dg_ls) < n :
        dg_ls.append(sum(dg_ls)); dg_ls = dg_ls[1:]; iteration += 1
    if sum(dg_ls) > n or len(dg_ls) == 1:   return False
    else:   return iteration
        
        
        


print(is_keith_number(n))