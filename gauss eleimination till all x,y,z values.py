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
# print(row)#Program to make / Replicate Gauss elimanation method

y2list=[]
for i in range(1,no_of_unknown):
    print(f"the y axis or cofficient is :{echosmatrix[i][1]}")
    y2=echosmatrix[i][1]
    y2list.append(y2)
    
print(y2list)
# yelimminatorcooficient=y2list[1]/y2list[0]
# print("Let see what it gives ==>",y2list[1],y2list[0],y2list[1]/y2list[0])
# new_y_list=[]#to store new eliminated y list
# for a,b in zip(echosmatrix[1],echosmatrix[2]):#to eliminate y same as x
#     new_y=b-yelimminatorcooficient*a
#     print(f"The new values of d3 is :{new_y}")
#     new_y_list.append(new_y)

newremovedy2=[]
for i in echosmatrix[1]:
    new_y=i/y2list[0]
    newremovedy2.append(new_y)

removed_y_list=[]
for a,b in zip(newremovedy2,echosmatrix[2]):
    removed_y=b-a*y2list[1]
    removed_y_list.append(removed_y)
    print(f"==> new removed y form matrix[2]is :{removed_y_list}")

echosmatrix.append(removed_y_list)
# echosmatrix.append(new_y_list)
del echosmatrix[2]
for row in echosmatrix:
    print(row)