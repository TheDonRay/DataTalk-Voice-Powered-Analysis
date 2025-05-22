#Libraries imported: Speech_recognition library. 
import speech_recognition as sr 
#import pandas library 
import pandas as pd #used for data manipulation and cleaning data. 

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
    
    
    
    #while loop 
    #i = enter_file
    while True: 
        enter_file = input("Please Enter file type")   
        if (enter_file.strip() == ""): 
            print("Please Try again and enter file type")
        elif enter_file.endswith(".csv") or enter_file.endswith(".xlsx") or enter_file.endswith(".xls"):
            return enter_file
        else: 
            print("Invalid file type. Please enter a valid file type.")
        
        

    
#calling the ask_user_for_file_type // we are not changing this first part. 
file_type = ask_user_for_file_type() #now remember we needed to do this to get the file type from the function to get the correct file. 
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#This is going to be the first section.  SECTION 1

#sections variables. # replace with options where their used to see the general overview of the data. 
section1 = "Section 1: General Overview of Data" 
section2 = "Section 2: Cleaning Data and Manipulating Data"

#in between sections call the mic function to check if user wants to switch between options and call that option. From user saying a certain answer. 

#gonna need to change this - to instead the first general overview of data section. 
#another idea is split it up by sections where the first part is general overview so we should do that first. 
#that means we have to change this instead of display to section 1 display and change it. 
def display_section(): 
    introduction_text = "Welcome to your Data Analyzing Tool. In this tool you'll have two sections, The first section is GOFD (General overview of Data) & your second section CD (cleaning Data & Data manipulation)"
    additional_text = "Below please speak into the mic whether you want 'section one' or 'section two'"

    print(introduction_text) 
    print(additional_text)
    print('\n')
    print(section1)
    print(section2)
    print('\n')

    
#calling display function to display the text
display_section() 



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def get_user_speech(): #this function just helps 
    recognizer = sr.Recognizer() #this recognizes the speech. 

#Now we have to read Microphone as source 
#listening to the speech and store in audio_text variable. 

    with sr.Microphone() as source: # this with statement what it basically does is that it ensures the resources are properly acquired and released, here it manages the Microphone resource. Then the sr.Microphone creates an instance of a microphone object that is used to capture audio input. 
        print("Calibrating to your background noise to hear you clearly...")
        print('\n')
        recognizer.adjust_for_ambient_noise(source, duration=2)  # Calibrates noise level
        print("Listening...")
        #create variable to hold for listening to user speech. 
        #global audio_text 
        try:
            audio_text = recognizer.listen(source, timeout = 15) #the timeout value is basically the max number of seconds to wait for speech to start. Phrase time limit is the maximum duration to capture audio after user stops speaking. 

            print("Done listening. Transforming data")
            print('\n')

            user_input = recognizer.recognize_google(audio_text) #recognize the users voice and what they said. 
            #using google speech recognition 
            print("Text that I heard from you!: " + user_input)
            return user_input #will help for easier comparison. 
        except Exception as e: 
            print("Sorry, I could not understand")
            return None 
        
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#calling the get speech function and setting it to the variable get_user_choice_for_section 
get_user_choice_for_section = get_user_speech() #note that we can make multiple calls to the same function to check something just remember to assign different variables to the function. 

#need to add a check right after this line to route based on the voice input 
if get_user_choice_for_section is not None: 
    choice = get_user_choice_for_section.lower() 
    if "section one" in choice or "section 1" in choice:
        section_1()
    elif "section two" in choice or "section 2" in choice:
        section_2()
    else:
        print("Could not recognize a valid section. Please try again.")
else:
    print("No input received. Please restart and try again.") 
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#predefining the sections here for the function. 

def section_1():  
    #going to display content for the general overview of data including mean null values etc. 
    #list some options 
    WelcomeText = "Here are some general options to get a general view and idea of your data please speak into the mic for which option you'd like" 
    print(WelcomeText)
    print('\n')  
    
    option1 = "1.) Show first 5 Rows to view in Data Frame" #head function
    option2 = "2.) Show last few rows to view in Data Frame" #tail function
    option3 = "3.) Show general trend of the data such as percentile, mean, median etc" #describe function
    option4 = "4.) Show missing null values in the Data Set" #issumnull.na function.  

    
    print(option1 ,'\n', option2, '\n', option3, '\n', option4, '\n') 
    print("Please choose an option !")
    
    choose_option = get_user_speech() #here im creating another variable to call the voice function to listen to the users input. 
    
    #Instead of making like a big if statement we can just make a dictionary of valid inputs smart to make it into a list and check like each of those sub parts in this list. 
    valid_options = [
        "Option 1", "option one", "option 1", "Option One", 
        "Option 2", "option two", "option 2", "Option Two", 
        "Option 3", "option three", "option 3", "Option Three", 
        "Option 4", "option four", "option 4", "Option Four" 
        ]
    
    #implement while loop for user to keep asking if they want another other options. 
    i = choose_option
    while(i not in valid_options): #same as saying check if what the user said if thats not matching up with the things in the list then ask them to try again. 
        print("Please choose a valid option!") 
        choose_option = get_user_speech()

    #if statement to check each option in that list index is equal to that sub list. - left of here. this is gonna be a if else statement calling each of the functions.  
    if (choose_option in ["Option 1", "option one", "option 1", "Option One"]): 
        print("You have selected Option 1") 
        option_1() #calling the first option for data cleaning. 
    elif (choose_option in ["Option 2", "option two", "option 2", "Option Two"]): 
        print("You have selected Option 2")
        option_2() #calling the second option for data cleaning.  
    elif(choose_option in ["Option 3", "option three", "option 3", "Option Three"]): 
        print("You have selected Option 3") 
        option_3() 
    elif(choose_option in ["Option 4", "option four", "option 4", "Option Four"]): 
        print("You have selected option 4") 
        option_4() 


def section_2():  
    #going to display content for the second part of the data for more of cleaning and manipulating data.  
    #section 2 is basically the same as section 1 so alot more implementation 
    Sectiontwo_welcome_text = "Welcome to Section 2. This is where you can clean your data"
    print(Sectiontwo_welcome_text) 
    print('\n') 
    
    #list of options still have to decide on which options to add  
    option1 = "1.) Remove any Null values present in the data set of given type." 
    option2 = "2.) Replace empty values with a value to make data more consistent."
    option3 = "3.) Change specific value in a specific column."
    
    print(option1 ,'\n', option2, '\n', option3, '\n') 
    print("Please choose an option !")
    
    #choose_option_ = get_user_choice_for_section() #calling this function to get the mic for users input notice looks the same but i added _
    choose_option = get_user_speech() 
 
    #make a list of the valid options for each type given.  
     valid_options = [
        "Option 1", "option one", "option 1", "Option One", 
        "Option 2", "option two", "option 2", "Option Two", 
        "Option 3", "option three", "option 3", "Option Three" 
        ]
    
    
    # Normalize the input
    def normalize_input(user_input):
        return user_input.lower().strip()

    user_choice = normalize_input(choose_option)

    # Re-prompt until valid option is selected
    while all(user_choice not in opts for opts in valid_options.values()):
        print("Please choose a valid option!")
        choose_option = get_user_speech()
        user_choice = normalize_input(choose_option)

    # Call corresponding section2 function
    if user_choice in valid_options["option 1"]:
        print("You have selected Option 1.")
        section2_option1()
    elif user_choice in valid_options["option 2"]:
        print("You have selected Option 2.")
        section2_option2()
    elif user_choice in valid_options["option 3"]:
        print("You have selected Option 3.")
        section2_option3()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# now we need to define the options for each of the sections to make sure that its good for the options to get called. 

def option_1(): #function to define the operation to get the data. 
    
    
    #Option 1 talks about showing first 5 rows in the data set so we can use the head function. 
    #remember we have to determine the file type to go into which file type we have or else we can get an error. 
    if (file_type.endswith(".csv")): #here im saying that 
        dataFrame = pd.read_csv(file_type) 
        print("Heres the first 5 rows of the data:") 
        print('\n')
        dataFrame.head() #this will give the first 5 rows to view. 
        print(dataFrame.head())
        print('\n')
        switch_option() # calling the switch functiion here 
        
    elif (file_type.endswith(".xlsx")): 
        dataFrame = pd.read_excel(file_type) # reading excel file type here. 
        print("Heres the first 5 rows of the data:")
        print('\n')
        dataFrame.head()  
        print(dataFrame.head())
        print('\n')
        switch_option() # calling the switch function here
        
    elif(file_type.endswith(".xls")): 
        dataFrame = pd.read_excel(file_type) 
        print("Heres the first 5 rows of the data:")
        print('\n')
        dataFrame.head() 
        print(dataFrame.head())
        print('\n')
        switch_option() #callling switch function here. 

def option_2(): 
    #option 2 talks about showing the last few rows of the data Frame 
    #same idea we have to check wether we are in the right file type for the data to be analyzed. 
    if (file_type.endswith(".csv")): #here im saying that 
        dataFrame = pd.read_csv(file_type) 
        print("Heres the last 5 rows of the data:") 
        print('\n')
        dataFrame.tail() #this will give the first 5 rows to view. 
        print(dataFrame.tail())
        print('\n')
        switch_option() #callling switch function here. 
        
        
    elif (file_type.endswith(".xlsx")): 
        dataFrame = pd.read_excel(file_type) # reading excel file type here. 
        print("Heres the last 5 rows of the data:")
        print('\n')
        dataFrame.tail()  
        print(dataFrame.tail())
        print('\n')
        switch_option() #callling switch function here. 
       
        
    elif(file_type.endswith(".xls")): 
        dataFrame = pd.read_excel(file_type) 
        print("Heres the last 5 rows of the data:")
        print('\n')
        dataFrame.tail() 
        print(dataFrame.tail())
        print('\n')
        switch_option() #callling switch function here. 

    
def option_3(): 
    #showing the general percentile and mean median of the data set that is inputed in the enter file area. 
    if (file_type.endswith(".csv")):
        dataFrame = pd.read_csv(file_type)  
        print("Here is the general trend of the data such as percentile, mean, mode, median and more !") 
        print('\n')
        dataFrame.describe()
        print(dataFrame.describe()) 
        print('\n')
        switch_option() #callling switch function here. 
      
        
    elif (file_type.endswith(".xlsx")): 
        dataFrame = pd.read_excel(file_type) # reading excel file type here. 
        print("Here is the general trend of the data such as percentile, mean, mode, median and more !")
        print('\n')
        dataFrame.describe()
        print(dataFrame.describe())
        print('\n')
        switch_option() #callling switch function here. 
        
    elif(file_type.endswith(".xls")): 
        dataFrame = pd.read_excel(file_type) 
        print("Here is the general trend of the data such as percentile, mean, mode, median and more !")
        print('\n')
        dataFrame.describe()
        print(dataFrame.describe())
        print('\n')
        switch_option() #callling switch function here. 
    
def option_4(): 
    if (file_type.endswith(".csv")):
        dataFrame = pd.read_csv(file_type)  
        print("Here is the missing values present in the data set") 
        print('\n')
        dataFrame.isnull().sum()
        print(dataFrame.isnull().sum())
        print('\n')
        switch_option() #callling switch function here. 
        
    elif (file_type.endswith(".xlsx")): 
        dataFrame = pd.read_excel(file_type) # reading excel file type here. 
        print("Here is the missing values present in the data set")
        print('\n')
        dataFrame.isnull().sum()
        print(dataFrame.isnull().sum())
        print('\n')
        switch_option() #callling switch function here. 
        
    elif(file_type.endswith(".xls")): 
        dataFrame = pd.read_excel(file_type) 
        print("Here is the missing values present in the data set")
        print('\n')
        dataFrame.isnull().sum()
        print(dataFrame.isnull().sum())
        print('\n')
        switch_option() #callling switch function here. 



#test function for the functionality of switching between sections and wether they want to repeat a section again  


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#global variables: 
#sw means switch option. 
sw_option1 = "Would you like to stay in Section 1? Please Reply with Yes or No"


def switch_option():  
    while True: 
        print(sw_option1)
        get_testing_answer = get_user_speech()# im calling the get_user_speech function. 
        if (get_testing_answer.lower() == "yes"): 
            section_1()
        elif(get_testing_answer.lower() == "no"): 
            section_2() 
            break 
        
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------         
#here storing the options for cleaning the actual data. This is for section 2. 

def section2_option1(): 
    
    if file_type.endswith(".csv"):
        dataFrame = pd.read_csv(file_type)
    elif file_type.endswith(".xlsx") or file_type.endswith(".xls"):
        dataFrame = pd.read_excel(file_type)
    else:
        print("Unsupported file format.")
        return 
    
    print("Removing rows with any null values...\n")
    cleaned_df = dataFrame.dropna()
    print("Cleaned DataFrame (first 5 rows):\n")
    print(cleaned_df.head())
    print("\nNull values removed successfully.")
    switch_option()

def section2_option2(): 
    
    if file_type.endswith(".csv"):
        dataFrame = pd.read_csv(file_type)
    elif file_type.endswith(".xlsx") or file_type.endswith(".xls"):
        dataFrame = pd.read_excel(file_type)
    else:
        print("Unsupported file format.")
        return 

    print("Replacing empty/null values with a default value...\n")
    
    default_value = input("Enter a value to replace nulls with (e.g., 0 or 'Unknown'): ")
    filled_df = dataFrame.fillna(value=default_value)
    
    print("Updated DataFrame (first 5 rows):\n")
    print(filled_df.head())
    print("\nEmpty values replaced.")
    switch_option()

def section2_option3(): 
    
    if file_type.endswith(".csv"):
        dataFrame = pd.read_csv(file_type)
    elif file_type.endswith(".xlsx") or file_type.endswith(".xls"):
        dataFrame = pd.read_excel(file_type)
    else:
        print("Unsupported file format.")
        return

    print("You can update a specific value in a column.")
    column_name = input("Enter the column name: ")
    old_value = input("Enter the value to replace: ")
    new_value = input("Enter the new value: ")

    if column_name not in dataFrame.columns:
        print(f"Column '{column_name}' not found in dataset.")
        return

    dataFrame[column_name] = dataFrame[column_name].replace(old_value, new_value)
    print(f"\nUpdated column '{column_name}' with new values. First 5 rows:\n")
    print(dataFrame.head())
    switch_option()
 
 
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
#THESE are essentially your callers to call everything. 
def check_first_section(): 
    if (get_user_choice_for_section == "section one" or get_user_choice_for_section == "section 1" or get_user_choice_for_section == "Section 1" or get_user_choice_for_section == "Section One"): 
        #were gonna call the other funciton to show the first section 1. 
        section_1()  #calling the section1 function

def check_second_section(): 
    if (get_user_choice_for_section == "section two" or get_user_choice_for_section == "section 2" or get_user_choice_for_section == "Section 2" or get_user_choice_for_section == "Section Two"): 
        section_2()

#have to call the check_first_section function and check_second_section / these two functions definetely kind of start it off to launch the whole program. 
check_first_section() #here we are actually calling the sections for them to check 
check_second_section() #calling the function for the checker for the next section type. 







