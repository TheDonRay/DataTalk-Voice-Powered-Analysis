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
        recognizer.adjust_for_ambient_noise(source, duration=2)  # Calibrates noise level
        print("Listening...")
        #create variable to hold for listening to user speech. 
        #global audio_text 
        try:
            audio_text = recognizer.listen(source, timeout = 15) #the timeout value is basically the max number of seconds to wait for speech to start. Phrase time limit is the maximum duration to capture audio after user stops speaking. 

            print("Done listening. Transforming data")

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



#now we have to create a checker where if section 1 is chosen we go into the options 

def check_first_section(): 
    if (get_user_choice_for_section == "section one" or get_user_choice_for_section == "section 1" or get_user_choice_for_section == "Section 1" or get_user_choice_for_section == "Section One"): 
        #were gonna call the other funciton to show the first section 1. 
        section_1()  #calling the section1 function

def check_second_section(): 
    if (get_user_choice_for_section == "section two" or get_user_choice_for_section == "section 2" or get_user_choice_for_section == "Section 2" or get_user_choice_for_section == "Section Two"): 
        section_2()

    

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
        print("Please choose a valid option !") 
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


    #need to add a checher if theyd like to do any other option for cleaning the data so need to come up with game plan to represent that code in order. 

#functions for first section 1 getting general view of data
def option_1(): #function to define the operation to get the data. 
    
    
    #Option 1 talks about showing first 5 rows in the data set so we can use the head function. 
    #remember we have to determine the file type to go into which file type we have or else we can get an error. 
    if (file_type.endswith(".csv")): #here im saying that 
        dataFrame = pd.read_csv(file_type) 
        print("Heres the first 5 rows of the data:") 
        print('\n')
        dataFrame.head() #this will give the first 5 rows to view. 
    elif (file_type.endswith(".xlsx")): 
        dataFrame = pd.read_excel(file_type) # reading excel file type here. 
        print("Heres the first 5 rows of the data:")
        print('\n')
        dataFrame.head()  
    elif(file_type.endswith(".xls")): 
        dataFrame = pd.read_excel(file_type) 
        print("Heres the first 5 rows of the data:")
        print('\n')
        dataFrame.head()
        

def option_2(): 
    #option 2 talks about showing the last few rows of the data Frame 
    #same idea we have to check wether we are in the right file type for the data to be analyzed. 
    pass
    
def option_3(): 
    pass
    
def option_4(): 
    pass


def section_2():  
    #going to display content for the second part of the data for more of cleaning and manipulating data.  
    #section 2 is basically the same as section 1
    pass 

#have to call the check_first_section function and check_second_section / these two functions definetely kind of start it off to launch the whole program. 
check_first_section() 
check_second_section()
        
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------







#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

