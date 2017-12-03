Flag_Values = {}
Flag_Terms = {}
Team_Names =[]
#See how many Temas and flags.
Total_Teams = int(input('How many Teams will be playing today?\n'))
Total_flags = int(input('How many flags will you be scoring today?\n'))

#Did functions so we can build a menue or GUI
#Team name figues out the teams names and puts them in a list.
def teamname(Total):
    for i in range(Total):
        i += 1
        tmp_teamname = input("What is Team %d's name?\n" % i)
        Team_Names.append(tmp_teamname)

#flags fiures out all the stats of the flags
def flags(tot_flags):
    for i in range(tot_flags):
        i += 1
        tmp_flagname = input('What will flag%d be called?\n' %i)
        tmp_term = input('What is the term for  %s??\n' % tmp_flagname)
        tmp_value = input('What is the Value of  %s?\n'% tmp_flagname)
        Flag_Values[tmp_flagname] = tmp_value
        Flag_Terms[tmp_flagname] = tmp_term

#This is just testing it
teamname(Total_Teams)
flags(Total_flags) 
print(Flag_Values)
print(Flag_Terms)
print(Team_Names)

#We need to figure out how to out put our team list to an html file
#Also how to store our dictonry so we can use it in the other programs.
