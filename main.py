# importing modules
import MDMod

# interface descriptor
print("MEDICAL DEJARGONIZER: Interface")
print("     Run '/commands' to view all commands.")

MDMod.line_space(1)

print("By running either '/translate' or '/describe,' you agree to our terms of service (viewable with '/tos.') Please email plushistoriae@gmail.com if there are innacuracies in the output of the program.")

MDMod.line_space(5)

while True: # 'forever loop' initialization
  user_input = input() # gains user input
  
  MDMod.line_space(1) # space after command input
  
  if user_input == "/about":
    print("ABOUT THE PROGRAM:")
    print("The MEDICAL DEJARGONIZER is a program to help patients understand a diagnosis or a condition.")
    MDMod.line_space(1)
    print("Originally, the MEDICAL DEJARGONIZER was part of a school project to create a project to help patients (specifically children from ages 5-15) communicate with doctors. While most groups in this project used pre-existing tools, our group (see credits) decided to create a tool from scratch. This project flourished mainly outside of school, where PlusHistoriae worked to create as high-quality of a project as possible.")
    MDMod.line_space(1)
    print("Work on this project mainly occured from March 16-19, 2023.")
    
    MDMod.line_space(2)
    
    print("FUNCTIONALITY:")
    print("The term 'dejargonize' refers to a form of translation from more complicated words to less compicated ones. This is acheived through a class system. Words are grouped into one of two classes -- complicated, and not complicated -- based off various details. If a word is complicated, the MEDICAL DEJARGONIZER will search for a less-complicated synonym, and replace the word.")
    MDMod.line_space(1)
    print("Another tool included in the MEDICAL DEJARGONIZER is a condition tool. If you have been diagnosed with a specific condition, the MEDICAL DEJARGONIZER will look for information on the condition and spit it back at you.")

    MDMod.line_space(2)
    
    print("PROGRAMMER AND OWNER: PlusHistoriae [Discord: PlusHistoriae#3739].")
    print("MANAGER AND TESTER: QuixotismFix.")
    print("PROPOSAL CREATORS: oliver twist AND FatGoose.")

    MDMod.line_space(2)
    
    print("IMPORTANT: ")
    print("We would reccomend reading the TOS.")
  
  elif user_input == "/commands": # adding /commands funtion
    print("'/about': a semi-detailed documentation of the project.")
    print("'/commands': lists commands and their format.")
    print("'/describe [condition]': gives a description of your medical [condition].")
    print("'/tos': explains the terms of service for this program.")
    print("'/translate [diagnosis]': dejargonizes your medical [diagnosis].")
  
  elif "/describe" in user_input:
    if user_input.count(" ") == 1:
      condition = user_input.split(" ")[1]
      print(condition)
    else:
      print("ERROR: the format of '/describe' is '/describe [condition],' and the input taken does not include the [condition] section. See '/commands' to see a list of commands and their format.")

  elif user_input == "/easteregg":
    print("hey. you've found the easter egg command. goodjbo mie firend")

  elif user_input == "/tos":
    MDMod.line_space(1)
    print("This program is not entirely accurate. It is accurate a large percentage of the time, but not at all completely accurate.")
    MDMod.line_space(1)
    print("Thus, the creators of this program, PlusHistoriae, QuixotismFix, oliver twist, and FatGoose are not liable for any damages caused by using the program or any assuming any incorrect output of this program to be the truth.")
    MDMod.line_space(1)
  
  elif "/translate" in user_input:
    if user_input.count(" ") == 1:
      diagnosis = user_input.split(" ")[1]
      print(diagnosis)
    else:
      print("ERROR: the format of '/translate' is '/translate [diagnosis],' and the input taken does not include the [diagnosis] section. See '/commands' to see a list of commands and their format.")

  MDMod.line_space(3) # spaces after command output