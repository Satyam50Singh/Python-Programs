#Lect - 13 Numpy Library part-1

import numpy as np # numpy is a package for maths operations.

print("Cos(3.14) : ",np.cos(np.pi))
print("Square root of 16 : ",np.sqrt(16))
print("log e^5.2 : ",np.log(np.exp(5.2)))  #Here we r using natural log i.e : loge

# we can create numpy array by converting lists
# this is a vector
vec = np.array([1,2,3]) #array() is used to convert lists to array.
print("\nvec : ",vec)
# we can create matrices by converting lists of lists
mat = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("")
print("mat :\n",mat)
print("\nTranspose of mat :\n",mat.T) ##Transpose
#There are lot of other way to create numpy array.
vec2 = np.arange(0,15)  ##0 is inclusive and 15 is exclusive

print("vec2 : ",vec2)
print('')
vec3 = np.arange(3,21,6) # 3 is inclusive and 21 is exclusive
print("vec3 : ",vec3)

#here we divide a range 0-5 in 10 divisions.
vec4 = np.linspace(0,5,10) ## 0,5 both are inclusive
print("vec4 : ",vec4)
print('')
#reshape() is change format for temporary purpose.
print("vec4.reshape(5,2) :\n ",vec4.reshape(5,2))
vec5 = vec4.reshape(5,2)
print("\nvec 5 : \n",vec5)
print("Original vec4 : ",vec4)

#methods to create matrix having value 0 & 1
mat2=np.zeros([5,3])
print("Zero Matrix : \n",mat2)
mat3=np.ones([3,5])
print("Matrix mat3 :\n",mat3)
print("")
#we can also access entries with logicals

rand_vec = np.random.randn(15)  #Random Vector

print("Random vector :\n",rand_vec)
print("\n",rand_vec>0)
print("Values Greater than 0 in rand_vec :\n",rand_vec[rand_vec>0])
print("")

rand_mat=np.random.randn(3,5) #Random Matrix 
print("Random matrix :\n",rand_mat)
print("Values Greater than 0 in rand_mat :\n",rand_mat[rand_mat>0])
print("")

print("Random vector :\n",rand_vec)
#Assign -5 to those pos whose value is less than 0.5
rand_vec[rand_vec>0.5]=-5
print("\n\n",rand_vec)

#Let's save some array on the disk.
np.save('Array_File',rand_mat)

#Save Array in zip format
np.savez('Zipped array file',rand_mat=rand_mat,rand_vec=rand_vec)


