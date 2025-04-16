#Program to make / Replicate Gauss elimanation method

User_input_equations=int(input("Enter the number of equation you have:"))#To store no of eqn from user
no_of_unknown=int(input("Enter the number of unknown values/variable:"))# to store no. of unknown
matrix=[]
newd1list=[]
echosmatrix=[]
for i in range(User_input_equations):
    list_of_equaton=list(map(float,input(f"Enter the cofficent and constant at last use spaces in between for equation{i} :").split( )))
    matrix.append(list_of_equaton)#Store/append the new list in mmatrix


for numbers in matrix[0]:
    new_list_of_equaton=round(numbers/matrix[0][0],2)#to make xofficient of x as 1 .
    newd1list.append(new_list_of_equaton)
print(f"===> the new simpler d1 equation is :{newd1list}")
# Now convert the matrix into echolog form like a down right stare case
print(f" ====> the first list is : {newd1list},the first cofficent of x is :{newd1list[0]}")
echosmatrix.append(newd1list)



for i in range(1,User_input_equations):#to help to run for n no of equations without writing again using range funtion.3
    list2=[]
    for a, b in zip(newd1list,matrix[i]):
        newx1cofficentmultiplier=matrix[i][0]
        print(a,b)
        newd2value=b-newx1cofficentmultiplier*a#to elementae x from matrix [1]
        print(newd2value)
        list2.append(newd2value)#to store new no x value of d2
    echosmatrix.append(list2)#to store all new simplefied equations making it a stare case equation to apply backward substitution


print("===>Bro i don't know how but it is working i think i have a chance to build something god for this world.")  
for rows in echosmatrix:
    print(rows)

#print(f"the new matrix [0] line is :{newd1list}")
# print(f"===> number of equation ={User_input_equations} , number of unknown ={no_of_unknown}")
# print(f"===> the matrix before solving is :")
# for row in matrix:
# print(row)