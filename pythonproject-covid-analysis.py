import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:\Users\user\Desktop\coding blocks(data science master course) all work self\country_wise_latest.csv")

def show_dataset():
    print(df)

def show_country():
    print(df[['Country/Region']])

def show_head():
    print(df.head())

def show_particularcountry(country1):
    print(df.iloc[country1])

#prints all the columns of the dataset
def show_all_columns():
    print(df.columns)


#prints the end of the dataset (tail of the dataset)
def show_tail():
    print(df.tail())

#describe function is used to get the insights from the data
#it provides the information of the dataset as - count,mean,std,max,etc.
def show_describe():
    print(df.describe())
    
#the dataset always contain null values which are useless and may not be used 
#so we will use isnull.sum function to get the sum of the null values if any
#print(df.isnull().sum())  #fortunately no null value in this dataset.

# RELATING VARIABLES USING SCATTERPLOT.
#further i will use it as a user manipulated ploting between different columns to generate insights.
#i will make it a function which will provide values or x and y from user and then plot the graph b/w the values
#hue can also be used to see the classification on the graph itself
def plot_diff_val(column1,column2):
    print(sns.relplot(x=column1, y=column2, data=df))
    plt.show()


#pairplot plots the relation with other feilds of the graph.
def plot_pair():
    sns.pairplot(df)
    plt.show()


#earlier the plotting that has been done is of dotted pattern type ,
#so now using the relplot function again but this time we specify the kind of plotting we want.
def plot_lineplot(column3,column4):
    sns.relplot(x=column3, y=column4, kind='line', data=df)
    plt.show()


#starting line of the main menu function
print("\n\t\t---DATA SCIENCE PROJECT---")
print("\n\t----COVID-19 ANALYSIS - WORLD'S DATA---- ")
print("\n\n Dataset used : World's data set on covid-19 is used in this data science project. The data set contains the data of all the countries under various column sections.")
print("\n\t -: This is a Menu Driven Project on Covid-19 Analysis :-")
print("\n\t The Project focus on bringing the relational plots and other information from the data set as per the user choice, the user can choose the options from the given menu. ")
print("\n\t The language used to build the project : Python \n The libraries used : seaborn, matplotlib.pyplot, pandas")

while(True):
    print("\n ---- M A I N  M E N U ----")
    print("\n 1. See the Data-Set Used.")
    print("\n 2. See First 5 rows of Data-set.")
    print("\n 3. See the tail of the Data-set.")
    print("\n 4. See all the columns of the Data-set.")
    print("\n 5. See the Described View of the Data-set.")
    print("\n 6. See the plot of columns of your choice.")
    print("\n 7. See the line plot of the columns of your choice.")
    print("\n 8. See the plot of the all the columns of the Data-set with different columns.")
    print("\n 9. See the information about particular country.")
    print("\n 10. Exit from the program")
    choice1 = int(input("\nEnter your choice : - "))

    if(choice1==1):
        show_dataset()
    elif(choice1==2):
        show_head()
    elif(choice1==3):
        show_tail()
    elif(choice1==4):
        show_all_columns()
    elif(choice1==5):
        show_describe()
    elif(choice1==6):
        print("\n The columns used in the data set are:- ")
        show_all_columns()
        column1 = str(input("Enter the value of column 1 :- "))
        column2 = str(input("Enter the value of column 2 :- "))
        plot_diff_val(column1,column2)
    elif(choice1==7):
        print("\n The columns used in the data set are:- ")
        show_all_columns()
        column3 = str(input("Enter the value of column 3 :- "))
        column4 = str(input("Enter the value of column 4 :- "))
        plot_lineplot(column3,column4)
    elif(choice1==8):
        plot_pair()
    elif(choice1==9):
        print("The countries in the Data set are : - ")
        show_country()
        country1 = int(input("Enter the index of the country : - "))
        show_particularcountry(country1)
    elif(choice1==10):
        break
    else:
        print("oops! incorrect choice ....")


1








