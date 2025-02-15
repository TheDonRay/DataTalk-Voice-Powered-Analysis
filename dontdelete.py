#Libraries imported: Speech_recognition library. 
import speech_recognition as sr 
#import pandas library 
import pandas as pd

#Initialize the recognizer class (for recognizing the speech) 

#set up a title kind of page to give user option to enter value. 
#gonna have the display but with no input so rather just use audio input to take that and use it to compare it to the logic 
#i guess kind of have to restart the layout.  


#start with asking user to input file. from their go into the dashboard. 
#Might have to create another function to input file type.  

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# this function is to get user file type. so we're not changing this. 
def ask_user_for_file_type(): 
    
    Welcome_Text = "Welcome to VDAT, Voice Data Analysis Tool. First thing we'd like you to do is enter your file type." 
    print(Welcome_Text)
    print('\n')
    example_file_type = "This can either be in the form csv (.csv) or excel (.xlsx) or (.xls)"
    print('\n')
    print(example_file_type)  
    
    enter_file = input("Please Enter file type")   
    
    #while loop 
    i = enter_file
    while (i.strip() == ""): 
        print("Please Try again and enter file type")
        enter_file = input("Please Enter file type") 
        print('\n')
        if (enter_file.endswith(".csv") or enter_file.endswith(".xlsx") or enter_file.endswith(".xls")): # the endswith function basically is used to check if a string ends with a specified suffix. 
            break 
        
    return enter_file 

#calling the ask_user_for_file_type
file_type = ask_user_for_file_type() #now remember we needed to do this to get the file type from the function to get the correct file. 
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#This is going to be the first section.  

#options variables. # replace with options where their used to see the general overview od the data. 
option1 = "1.) "
option2 = "2.) " 
option3 = "3.) "  
option4 = "4.) "
option5 = "5.) "
#in between sections call the mic function to check if user wants to switch between options and call that option. From user saying a certain answer. 

#gonna need to change this - to instead the first general overview of data section. 
#another idea is split it up by sections where the first part is general overview so we should do that first. 
#that means we have to change this instead of display to section 1 display and change it. 
def display(): 
    introduction_text = "Welcome to your Data Analyzing Tool. In this tool you'll have two sections, The first section is GOFD (General overview of Data) & your second section CD (cloning Data)"
    additional_text = "Below please speak into the mic whether you want 'section one' or 'section two'"

    print(introduction_text) 
    print(additional_text)
    print('\n')
    print(option1)
    print('\n')
    print(option2)
    print('\n')
    print(option3) 
    print('\n') 
    print(option4)
    print('\n')
    print(option5)
    
#calling display function: 
display() 


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def get_user_speech(): #this function just helps 
    recognizer = sr.Recognizer() #this recognizes the speech. 

#Now we have to read Microphone as source 
#listening to the speech and store in audio_text variable. 

    with sr.Microphone() as source: # this with statement what it basically does is that it ensures the resources are properly acquired and released, here it manages the Microphone resource. Then the sr.Microphone creates an instance of a microphone object that is used to capture audio input. 
        print("Calibrating to your background noise to hear you clearly...")
        recognizer.adjust_for_ambient_noise(source, duration=2)  # Calibrates noise level
        print("Listening...")
        #create variable to hold for listening to user speech. 
        #global audio_text 
        try:
            audio_text = recognizer.listen(source, timeout = 5) #the timeout value is basically the max number of seconds to wait for speech to start. Phrase time limit is the maximum duration to capture audio after user stops speaking. 

            print("Done listening. Transforming data")

            user_input = recognizer.recognize_google(audio_text) #recognize the users voice and what they said. 
            #using google speech recognition 
            print("Text that I heard from you!: " + user_input)
            return user_input #will help for easier comparison. 
        except Exception as e: 
            print("Sorry, I could not understand")
            return None

#call this function to get_user_speech 
#get_user_speech() 

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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
        
''' use this function for the cleaning data section so we have to move this around. 
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

    
