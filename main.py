import os
import botnikkk as n

#Fromating root
def format_root(root) :
    if type(root) is float :
        if root < 0 :
            factor = -1
        else :
            factor = 1
        try:
            root = float(str(root).strip('-')[0:5])*factor
        except :
                None
        root_check = (root).as_integer_ratio()
        if len(str(root_check[0])) and len(str(root_check[1])) < 3 :
            root = root_check
            if root[1] != 1 :
                root = f"{root[0]}/{root[1]}"
            else:
                root = root[0]

    return root

#checking degree and soting equation
def degcheck(equation) :
    #generalizing the equation by + sign
    new_equation = '' 
    for i in equation :
        if i == "-" : 
            new_equation += "+" + i
        else :
            new_equation += i

    #spliting the equation to acquire singular variables
    equation_variables = new_equation.split("+")
    new_equation_variables = []
    for i in equation_variables :
        i = str(i).strip()
        new_equation_variables.append(i)
    equation_variables = new_equation_variables
    while '' in equation_variables :
        equation_variables.remove('')

    #checking the degree of the equation
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

    #Quadratic eqn
    if largest_degree_so_far == 2 :
        deg2(equation_variables)



#quadratic equation
def deg2(equation_variables) :

    #extracting coffecients and contants from the equation
    a,b,c = 0,0,0
    for i in equation_variables :
        #removing empty space from the variable
        if " " in i :
            i = str(i).split()
            string = " "
            for j in i :
                string += str(j)
            i = string

        #extracting value of a
        if "x^2" in i :
            if i[:-3] == '' :
                a = 1
            elif '-x' in i :
                a = -1
            else :
                a = int(i[:-3])

        #extracting value of b
        elif "x" in i :
            if i[:-1] == '' :
                b = 1
            elif '-x' in i :
                b = -1 
            else :
                b = int(i[:-1])

        #extracting value of c       
        else :
            if i == '-' :
                i = -1 
            c = int(i) 

    #calculating the discriminant
    discriminant = (b**2) - (4*a*c)

    #Real roots
    if discriminant >= 0 :

        #calculating roots
        underoot_part = (discriminant)**(1/2) 
        root1 = ((-b) + underoot_part)/(2*a)
        root2 = ((-b) - underoot_part)/(2*a)

        #Fromating roots
        root1 = format_root(root1)
        root2 = format_root(root2)

    #Imaginary roots
    elif discriminant < 0 :

        discriminant *= -1 

        #sorting real and imaginary parts of the roots
        imaginary_part = (discriminant **(1/2))/(2*a)
        real_part = (-b)/(2*a)

        #Formating parts
        real_part = format_root(real_part)
        imaginary_part = format_root(imaginary_part)

        #Formating roots
        root1 = f"{real_part} + {imaginary_part}i"
        if imaginary_part < 0 :
            imaginary_part *= -1
            root2 = f"{real_part} + {imaginary_part}i"
        else :
            root2 = f"{real_part} - {imaginary_part}i"

    n.centre(f"The roots of the equation are : {root1} and {root2}")



#cool entry screen 
file = open("design.txt",encoding= "utf8")
lines = file.readlines()
file.close()
#Forever loop
equation = ''
while equation != 'exit' :
    middle = n.get_alignments()['left_align']*" "
    os.system('cls')
    string = ""
    for i in  lines : 
        print(middle + i.strip('\n'))
    equation = n.format_input("Enter a equation or Type 'exit' to exit")
    if str(equation).lower() != 'exit' :
        degcheck(equation) 
        while str(equation).lower() != 'exit' :
            equation = n.format_input("Enter a equation or Type 'exit' to exit")
            if str(equation).lower() != 'exit' :
                degcheck(equation) 
    else :
        n.centre("Exited the calculator", "-")
        break
