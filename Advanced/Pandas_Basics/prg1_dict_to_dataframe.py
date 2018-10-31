import pandas as pd # import the pandas module 

# create a simple dictionary holding some key value pairs
my_dict = {
          "col1":[1,2,3,4],
          "col2":[5,6,7,8],
          "col3":[9,10,11,12],
          "col4":[13,14,15,16]
          }
print(my_dict) # view the dictionary

#convert dictionary into a dataframe
dataframe = pd.DataFrame(my_dict) # use pandas inbuilt DataFrame method

print(dataframe) # view the created dataframe
