def fig_a():
    for i in range(5):
        print(" "*i + "*"*(5-i))


def fig_b():
    for i in range(5):
        print("*"*(i+1) + " "*(5-i))


def fig_c():
    for i in range(5):
        if i < 3:
            print(" "*i + "*"*(5-2*i) + " "*i)
        else:
            print(" "*5)


def fig_d():
    for i in range(5):
        if i > 1:
            print(" "*(4-i) + "*"*(2*i-3) + " "*(4-i))
        else:
            print(" "*5)


def fig_e():
    for i in range(5):
        if i < 3:
            print(" "*i + "*"*(5-2*i) + " "*i)
        else:
            print(" " * (4 - i) + "*" * (2 * i - 3) + " " * (4 - i))


def fig_f():
    for i in range(5):
        if i < 2:
            print("*"*(i+1) + " "*(3-2*i) + "*"*(i+1))
        elif i == 2:
            print("*"*5)
        else:
            print("*" * (5 - i) + " " * (2 * i - 5) + "*" * (5 - i))


def fig_g():
    for i in range(5):
        if i <= 2:
            print("*" * (i + 1) + " " * (4 - i))
        else:
            print("*" * (5 - i) + " " * i)


def fig_h():
    for i in range(5):
        if i <= 2:
            print(" " * (4 - i) + "*" * (i + 1))
        else:
            print(" " * i + "*" * (5 - i))


def fig_i():
    for i in range(5):
        print("*" * (5 - i) + " " * i)


def fig_j():
    for i in range(5):
        print(" " * (4 - i) + "*" * (i + 1))


def menu_():
    print("""-----Menu-----
         ***
    a =>  **
           *
           
         *  
    b => ** 
         ***
         
         ***
    c =>  * 
    
    
    
    d =>  * 
         ***
         
         ***
    e =>  * 
         ***
         
         * *
    f => ***
         * *
         
         *  
    g => ** 
         *
         
           *
    h =>  **
           *
           
         ***
    i => **
         *
           
           *
    j =>  **
         ***
         """)


def show(fig):
    function = "fig_" + fig + "()"
    eval(function)


def run():
    menu_()
    user_input = input("Zadejte požadovaný čtvereček: ")
    show(user_input)


run()
