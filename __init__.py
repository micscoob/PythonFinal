#Import needed things for flask and email
from flask import Flask, request, redirect, render_template
import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

app = Flask(__name__)
Flag_dic = {}
Team_dic = {}
team_names = []

class print_score(object):
    ###This emials us the scores that def score() generates.###
    def email():
        fromaddr = "pythonfinal2017@gmail.com" #add your own emil
        toaddr = "pythonfinal2017@gmail.com"
 
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Teamscores"
        body = "These are the scores of the team"
        msg.attach(MIMEText(body, 'plain'))
        filename = "teams.csv"
        attachment = open("./teams.csv", "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
        msg.attach(part)
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddr, "Thisisapassword123!")
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            email =('email sent')
            server.quit()
            return render_template("test.html",email=email)
        except:
            email = ('unable to send email')
            return render_template("test.html",email=email)
            
    def score(): ##This makes the teams.csv that can be emailed
        with open("teams.csv", "w") as file:
            
            for k, v in Team_dic.items():
                dictionary_content = k + "," + ('%s'%v) + "\n"
                file.write(dictionary_content)
##FLASK##
#In flask you use @app.route() to define a route on your server.
#The fuctions after run after the route is exucuted.
#at the end for the functions you need to return render_templates. 
#this returnes a file located in /var/www/FlaskApp/FlaskApp/Templates.
#the variables defied after it are ones on the html page.

@app.route("/")
def homepage():
    text = 'Points:'
    total = 0 #points that team has
    return render_template("index.html", text=text,Team_dic=Team_dic)

@app.route("/Setup", methods=['GET','POST'])#You get and post to get text from text box
def setup_padge():
    if request.method == 'POST':
        tmp_flags = {}
        tmp_team_points = {}
        
        flag_name = request.form['flag']
        flag_value = request.form['flagvalue']   #request.form 'NAME' name is what the variable in html are.
        flag_points = request.form['flagpoints']
       
        flag_points = int(flag_points)  #convert to int
        
        tmp_flags[flag_value] = flag_points
        Flag_dic[flag_name] = tmp_flags
        
        
        Team_name = request.form['team_name']
        Team_points = 0
        Team_dic[Team_name] = Team_points
        
        team_names.append(Team_name)
        return redirect("/Setup")
        
    if request.method == 'GET':
            text = 'Setup'
            return render_template("setup.html",text=text)

@app.route('/points',methods=['GET','POST']) #This will look through the dic and add points to teams accordingly..
def points():
    if request.method == 'POST':
        flag_name = request.form['flag']
        flag_value = request.form['flagvalue']
        team_name = request.form['Teamname']
        #pulls sub dic out.
        #pulls out the team name and points they have
        tmp_dic = Flag_dic.get(flag_name,None)
        points = Team_dic.get(team_name,None)
        
        if tmp_dic.get(flag_value, None) != None:
            points = tmp_dic.get(flag_value,None) + points
            tp = {team_name:points}
            Team_dic.update(tp)
            return redirect("/")
        else:
            text = 'You done goof'
            return render_template("points.html",text=text)

    if request.method == 'GET':
        return render_template("points.html")
    


@app.route('/About')
def aboutpage():
    return render_template("about.html")
    
@app.route('/test')
def test():  # Use this page for testing
    text = 'This is a test page'
    return render_template("test.html",Team_dic=Team_dic,team_names=team_names, text=text,Flag_dic=Flag_dic)

@app.route('/print') #prints
def score():
    text= 'Print secseful'
    print_score.score()
    return render_template("test.html",text=text)
    
@app.route('/email') #emails
def email():
    emails = 'Email sucsessful'
    print_score.email()
    return render_template("test.html")

    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=33)
 
