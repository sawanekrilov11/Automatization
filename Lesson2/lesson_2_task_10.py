def bank(x,y): # x - рубли y - года 
    for a in range(y):
        x = x + (x * 0.1) # 0.1 = 10%
    return print(round(x,1))

bank(9999,12)