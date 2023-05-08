
bb = [1,2,3,4,5,6]
def cc(n):
    n[0], n[1] = n[1], n[0]
    
    return n
print(cc(bb))