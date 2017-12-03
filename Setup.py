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
        tmp_flagname = ('flag%d' % i)
        tmp_term = input('What is the term for  %s??\n' % tmp_flagname)
        tmp_value = input('What is the Value of  %s?\n'% tmp_flagname)
        Flag_Values[tmp_flagname] = tmp_value
        Flag_Terms[tmp_flagname] = tmp_term
##HTML File is created in the same directory as your program is runned from.
def createhtml():
    f = open('helloworld.html','w')
    start =("""
                <html>
                <head></head>
                <body>""")
    end = ( """</body> </html>""")
    f.write(start)
    for i in Team_Names:
        middle = ("""<p>%s points are <p>
            <a href="/python.py/">Click here to enter your points</a>
                            """ %i)
        f.write(middle)
    f.write(end)
        
#This is just testing it
teamname(Total_Teams)
flags(Total_flags)
createhtml()

#Also how to store our dictonry so we can use it in the other programs.
