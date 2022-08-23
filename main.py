def degcheck(equation) :
    
    equation = str(equation)

    if "-" in equation : 
        for i in equation :
            print(i)
            if i == "-" : 
                index = equation.index(i)
                print(equation[:index],"and", equation[index:])
                new_equation = equation[:index] + "+" + equation[index:] 

            
    print(new_equation)
    equation_variables = equation.split("+")

    for i in equation_variables :
        index = equation_variables.index(i)
        i = str(i).split()
        equation_variables[index] = i[0]

    largest_degree_so_far = 0 
    for i  in equation_variables :
        try:
            if int(i[-1]) > largest_degree_so_far and "x" in i:
                largest_degree_so_far = int(i[-1])
        except :
            if i[-1] == "x" and largest_degree_so_far < 1 :
                largest_degree_so_far = 1
            elif "x" not in i and largest_degree_so_far < 1 :
                continue

    if largest_degree_so_far == 2 :
        deg2(equation_variables)



def deg2(equation_variables) :
    print(equation_variables)
    for i in equation_variables :
        if "x^2" in i :
            if i[:-3] == '' :
                a = 1
            else :
                a = int(i[:-3])
        elif "x" in i :
            if i[:-1] == '' :
                b = 1 
            else :
                b = int(i[:-1])
        else : 
            c = int(i) 
    discriminant = (b**2) - (4*a*c)
    if discriminant >= 0 : 
        root1 = (-b + (discriminant **1/2))/(2*a)
        root2 = (-b - (discriminant **1/2) )/(2*a)
    elif discriminant < 0 :
        discriminant *= -1 
        imaginary_part = (discriminant **1/2)/(2*a)
        real_part = (-b)/(2*a)
        root1 = str(real_part) + " + " + str(imaginary_part) + "i"
        root2 = str(real_part) + " - " + str(imaginary_part) + "i"

    print(discriminant)
    print("The roots of the equation are :", root1, "and",  root2)

equation = input("Enter equation\n- ")
degcheck(equation) 
