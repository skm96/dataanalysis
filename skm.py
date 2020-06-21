
"""
Created on Sun Jun 21 10:54:11 2020

@author: Soumya Kanti Mandal
"""
import pandas as pd
from bokeh.plotting import figure , output_file,show,output_notebook  #it is used for visulization
output_notebook()

#this fuction is used which show an html file as output
def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
    show(p)
    
#the gdp and unemployment data given in the dictionary 
links={'GDP':'gdp.csv',\
       'unemployment':'employ.csv'}

#read gdp data
df1=pd.read_csv(links['GDP'])
print("The gdp details that we import-----\n",df1.head())
print('\n')
#read unemployment data
df2=pd.read_csv(links['unemployment'])
print("The unemployment details that we import----- \n",df2.head())
print('\n')

 #it show in boolean value  true that are upper 8.5 & false that are lower than 8.5
#dfnew=[df['unemployment']>8.5]   
#dfnew
 
 #it show the values of >8.5 only
dfnew=df[df2['unemployment']>8.5]
print("display unemployment >8.5---- \n",dfnew)
print('\n')

#====== for gdp =======
#now we use the dashboard function parameter x  to create new dataframe with column 'date' 
x=pd.DataFrame(df1,columns=['date'])    #we take 'df1' where we store the gdp 
print("new column column date created \n",x.head())
print('\n')

#now we use gdp_change  to create new dataframe with column 'change-current' 
  #we take 'df1' where we store the gdp
gdp_change=pd.DataFrame(df1,columns=['change-current'])
print("new change-current column  date created \n",gdp_change.head())
print('\n')

#======for unemployment ========
#Create a new dataframe with the column 'unemployment'  called unemployment from the dataframe that contains the unemployment data.
unemployment =pd.DataFrame(df2,columns=['unemployment']) # Create your dataframe with column unemployment
print("new unemplyment column  date created \n",unemployment.head())
print('\n')


#giving the dashboard a string title, and assign it to the variable title
title ='Unemployment with Gdp' # Give your dashboard a string title

# the make_dashboard function create a html file which stored in directory after the make_dashboard call 
file_name = "index2.html"
#we can run this in ebsite to see the values


# the parameters in the following functions what we created
# x=x what i created as a 'date' column
#gdp_change=gdp_change what i created as 'change-current column'
#unemployment=unemployment what i created as a 'unemployment column
#file_name=file_name here we store the analysis data as a html file 
make_dashboard(x=x, gdp_change=gdp_change, unemployment=unemployment, title=title, file_name=file_name)

print('done')
