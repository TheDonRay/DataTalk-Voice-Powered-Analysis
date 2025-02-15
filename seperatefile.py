
#placing this code later down the program 


'''
# these two functions are going to be used for the first section along with some other functions for the general overview of the data. 
#Note that the functions for the actual data analyzing will come before hand and then called in the check_voice_answer function. 
def ShowingNull_values(): 
    #need to do if statement to check wether file type is csv or xlsx. 
    if (file_type.endswith(".csv")): 
        data_set = pd.read_csv(file_type) 
        data_set.isnull().sum() 
        print(data_set.to_string()) #truncates the data 
    # have to do this to check for other file types as well. 
    elif (file_type.endswith(".xlsx")): 
        data_set = pd.read_excel(file_type) 
        data_set.isnull().sum()  
        print(data_set.to_string())   
    # basically doing the same thing for the xls function. 
    elif (file_type.endswith(".xls")):   
        data_set = pd.read_excel(file_type) 
        data_set.isnull().sum()  
        print(data_set.to_string()) 
    

def showingDataFrame_statistics(): #using the describe function to in pandas to represent the data. 
    #again we basically have to do the same thing as the previous code but change the function to do the describe null function. 
    if (file_type.endswith(".csv")): 
        data_set = pd.read_csv(file_type) 
        data_set.describe() 
        print(data_set.to_string())  
    elif(file_type.endswith(".xlsx")): 
        data_set = pd.read_csv(file_type) 
        data_set.describe() 
        print(data_set.to_string())  
    elif(file_type.endswith(".xls")): 
        data_set = pd.read_csv(file_type) 
        data_set.describe() 
        print(data_set.to_string())  
        
        
#---------------------FUNCTION BELOW USED FOR SECOND SECTION WHICH IS CLEANING DATA SECTION -----------------------------------------------------------------------------# 
        
use this function for the cleaning data section so we have to move this around. 
def RemovingNullValues(): 
    if (file_type.endswith(".csv")): 
        data_set = pd.read_csv(file_type) 
        data_set.dropna(inplace = True) 
        print(data_set.to_string())  
    elif(file_type.endswith(".xlsx")): 
        data_set = pd.read_csv(file_type) 
        data_set.dropna(inplace = True) 
        print(data_set.to_string())  
    elif(file_type.endswith(".xls")): 
        data_set = pd.read_csv(file_type) 
        data_set.dropna(inplace = True)
        print(data_set.to_string())  
   ''' 


#going to have to move this function above to check for if user wants section 1.   
''' 
#global getuser_choice 
getuser_choice = get_user_speech()

def check_voice_answer(): 
    
    if getuser_choice == "option one" or getuser_choice == "option 1": 
        #here would be another function to call for the data analyzing part 
        print("Sounds good! Here is your data with the shown null values in the Dataset/DataFrame: ") 
        #here we call the function to show the null values. 
        ShowingNull_values() 
        print('\n')
        
    elif getuser_choice == "option two" or getuser_choice == "option 2": 
        print('\n')
        print("Here is the data's key statistical metrics such as: percentile, mean, mode, median, Standard Deviation:") 
        #here we call the function to show the null values.
        showingDataFrame_statistics() 
        
    elif getuser_choice == "option three" or getuser_choice == "option 3": 
        print('\n')
        print("We've removed the ")
        #RemovingNullValues()  
    elif (getuser_choice == " "): 
        print("Sorry I didn't get that")

#call the check_voice_answer function 
check_voice_answer() 


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
