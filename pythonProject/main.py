def fig_a():
    for i in range(5):
        print(" "*i + "*"*(5-i))

def fig_b():
    for i in range(5):
        print("*"*(i+1) + " "*(5-i))

def fig_c():
    for i in range(5):
        if i<3:
            print(" "*i + "*"*(5-2*i) + " "*i)
        else:
            print(" "*5)