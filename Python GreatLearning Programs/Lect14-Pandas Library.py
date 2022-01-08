#Lect - 14 Pandas Library Part - I

##Pandas
# Pandas package is used for data managing
# Pandas is mainly used for creating two new data type : series ,dataframe
# A dataframe is made up of several series .Each column of a dataframe is a series.
# We can name each column and row of a dataframe
# Pandas also has SQL-functions for merging ,joining and sorting dataframes.

#install pandas library by using command : pip install pandas
import pandas as pd
import numpy as np

##We can create series by converting a list ,or numpy array.
mylist=[3,7,8,1.2,-4,87]
myarray=np.array(mylist)

my_series1=pd.Series(data=mylist) #Series - 01
my_series2=pd.Series(data=myarray) #Series - 02
print("my_series1 :\n\n",my_series1)
print("my_series2 :\n",my_series2)

#we can also access indiviual enries the same way as we do in list and array
print("Value at third position : ",my_series1[2])

#we can add labels to the entries of a series.
my_labels=['First','Second','Third','Fourth','Fifth','Sixth']
my_series3=pd.Series(data=myarray,index=my_labels)
print("\nmy_series3 :\n")
print(my_series3)

#we need not be explicit about the entries
my_series4=pd.Series(myarray,my_labels)
print("\nmy_series4 :\n")
print(my_series4)

#we can also access entries using the index labels
print("\nmy_series4['Second'] : ",my_series4['Second'])

#We can do Maths on series
my_series5=pd.Series(data=[23,2,6,8.4,-2],index=['First','Third','Fourth','Fifth','Sixth'])
print("\nmy_series5 :\n")
print(my_series5)

print("\nAddition of my_series4 + my_series5\n")
print(my_series4 + my_series5)
print("\nSubtraction of my_series4 + my_series5\n")
print(my_series4 - my_series5)
print("\nMultiplication of my_series4 + my_series5\n")
print(my_series4 * my_series5)


#we can combine series to create dataframe using the concat fn.
df1=pd.concat([my_series4,my_series5],axis=0,sort=True)
print("\ndf1 with axis=0,sort=True \n")
print(df1)

df1=pd.concat([my_series4,my_series5],axis=1,sort=False)
print("\ndf1 with axis=1,sort=False \n")
print(df1)

# we can create a new dataframe.
df2=pd.DataFrame(np.random.randn(5,5))
print("df2\n")
print(df2)

# Give labels to its rows and column.
df3=pd.DataFrame(np.random.randn(4,4),index=['First row','Second row','Third row','Fourth row'],
                 columns=['First col','Second col','Third col','Fourth col'])
print(df3)
print("")
#we can access indiviual series in a data frame.
print(df3['First col'])
print("")
print(df3[['Second col','Third col']])
print("")
#we can access rows of a dataframe.
print(df3.loc['First row'])
print("")
print(df3.iloc[2])

#Subset of data frame.
print("")
print(df3.loc[['First row','Third row'],['First col','Fourth col']])


