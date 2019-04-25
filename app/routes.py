from flask import render_template, flash, redirect, url_for, request,session
from app import app
from app.forms import LoginForm, RegistrationForm, ProjectForm,TaskForm,SandBox,ConvertToBackLog
import json, sys


#TODO Merge with Microsoft Project
#TODO merge github
#TODO implement modals
#TODO work on cleaning up interface
#TODO add some features if we can
#TODO Implement database features with applet security


current_user=""
#dataString='/Users/lzhou/Documents/group7/app/data/'
#dataString='C:/Users/benma/Desktop/cs442/code/v2/group7/app/data/'
#dataString='C:/Users/swald/group7/app/data/'
dataString='C:/Users/Tian/Documents/UIC/CS/CS442/Repository/group7/app/data/'
@app.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()
    if request.method == 'POST':
        current_user=request.form["username"]
        return redirect(url_for('projectList'),current_user=current_user)
    else:
        return render_template("index.html",title="FireScrum",form=form,current_user="")


@app.route('/signUp', methods=['GET', 'POST'])
def signUpPage():
    form = RegistrationForm()
    if request.method == 'POST':
        nameF = request.form["nameF"]
        nameL = request.form["nameL"]
        email = request.form["email"]
        uname = request.form["username"]
        pword = request.form["password"]

        account = {"username":uname,"fname":nameF,"lname":nameL,"email":email,"password":pword}

        with open(dataString+"account.json",'r') as file:
            accounts = json.loads(file.read())

        accounts.append(account)

        with open(dataString+"account.json",'w') as fileout:
            fileout.write(json.dumps(accounts, indent=2))

        return redirect(url_for('home'))

    return render_template("signUp.html",form=form)


def credentialCheck(username, password):
    with open(dataString+"account.json", 'r') as file:
        accounts = json.loads(file.read())

    #print(accounts)


    for user in accounts:
        if user["username"] == username and user["password"] == password:
            return user

    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        current_user = request.form["username"]
        current_pass = request.form["password"]

        user = credentialCheck(current_user, current_pass)
        if user:

            #print(user)
            return redirect(url_for('projectList', current_user= current_user))
        else:
            #print("invalid user")

            return render_template("index.html",title="FireScrum",form=form,current_user="")

        #if current_user.is_authenticated():
        #    g.user = current_user.username
        #return redirect(url_for('projectList', current_user= current_user))
    else:
        return render_template('signIn.html', title='Sign In', form=form,current_user=current_user)

@app.route('/about')
def about():
    return render_template("aboutfirescrum.html")

@app.route('/<current_user>/<projectName>/accountSettings', methods=['GET', 'POST'])
def modifyAccount(current_user,projectName):
    if request.method == 'POST':
        description=request.form["taskGoal"]
        #form
    fileP = dataString+projectName+'.json'
    filein = open(fileP, 'r')
    #print(fileP)
    #print(filein)
    proj = json.loads(filein.read())
    #print(proj)
    return render_template("accountSettings.html", current_user=current_user,proj=proj)

@app.route('/<current_user>/<projectName>/CurrentSprint')
def projectCurrentSprint(current_user, projectName):
    fileP = dataString+projectName+'.json'
    filein = open(fileP, 'r')
    #print(fileP)
    #print(filein)
    proj = json.loads(filein.read())
    #print(proj)
    return render_template("currentSprint.html", current_user=current_user,proj=proj)

@app.route('/<current_user>/<projectName>/<Issue_Name>/CreateTask', methods=['GET', 'POST'])
def projectcreateTask(current_user, projectName, Issue_Name):
    fileP = dataString+projectName+'.json'
    filein = open(fileP, 'r')
    #print(fileP)
    #print(filein)
    proj = json.loads(filein.read())
    #print(proj)
    if request.method == 'POST':
        Issue_Name3 = request.form['taskName']
        Description = request.form['taskGoal']
        time= request.form['storyPoint']
        assignedTo = request.form['assignedTo']
        newTask={'Issue_Name':Issue_Name3,'time':time,'Description':Description,'assignedTo':assignedTo}
        todList=proj['currentSprint']['TODO']
        for idea in todList:
            if idea['Issue_Name'] == Issue_Name:
                idea['Tasks']['TODO'].append(newTask)
                with open(fileP,'w') as fileout:
                    fileout.write(json.dumps(proj, indent=2))
                return redirect(url_for('projectCurrentSprint', current_user=current_user, projectName= proj['name'] ))
        todList=proj['currentSprint']['In_Progress']
        for idea in todList:
            if idea['Issue_Name'] == Issue_Name:
                idea['Tasks']['TODO'].append(newTask)
                with open(fileP,'w') as fileout:
                    fileout.write(json.dumps(proj, indent=2))
                return redirect(url_for('projectCurrentSprint', current_user=current_user, projectName= proj['name'] ))
    form=TaskForm()
    return render_template("CreateTask.html", current_user=current_user,proj=proj,Issue_Name2=Issue_Name,form=form)

@app.route('/<current_user>/<projectName>/Sprints')
def projectSprints(current_user, projectName):
    fileP = dataString+projectName+'.json'
    filein = open(fileP, 'r')
    #print(fileP)
    #print(filein)
    proj = json.loads(filein.read())
    #print(proj)
    return render_template("sprints.html", current_user=current_user,proj=proj)

@app.route('/<current_user>/<projectName>/Discussion')
def talkBox(current_user, projectName):
    fileP = dataString+projectName+'.json'
    filein = open(fileP, 'r')
    proj = json.loads(filein.read())
    #print(proj)
    #print("\n\nDiscussion\n\n")
    discussion = proj["Discussion"]
    return render_template("discussionBoard.html", current_user=current_user,proj=proj)

@app.route('/<current_user>/projects')
def projectList(current_user):
    filein = open((dataString+'projects.json'), 'r')
    #print (filein.read(), file=sys.stdout)
    filein.seek(0,0)
    projList = json.loads(filein.read())
    return render_template("projects.html",projectList=projList, current_user=current_user)

@app.route('/<current_user>/<projectName>')
def projectSplash(current_user, projectName):
    fileP = dataString+projectName+'.json'
    filein = open(fileP, 'r')
    #print(fileP)
    #print(filein)
    proj = json.loads(filein.read())
    #print(proj)
    return render_template("projectDash.html", current_user=current_user,proj=proj)

@app.route('/<current_user>/<projectName>/BackLog')
def projectBackLog(current_user, projectName):
    fileP = dataString+projectName+'.json'
    filein = open(fileP, 'r')
    #print(fileP)
    #print(filein)
    proj = json.loads(filein.read())
    #print(proj)
    return render_template("backlog.html", current_user=current_user,proj=proj)

@app.route('/<current_user>/<projectName>/burnupchart')
def projectBurnupChart(current_user, projectName):
    fileP = dataString+projectName+'.json'
    filein = open(fileP, 'r')
    #print(fileP)
    #print(filein)
    proj = json.loads(filein.read())
    #print(proj)
    return render_template("burnupchart.html", current_user=current_user,proj=proj)

@app.route('/<current_user>/<projectName>/issues')
def projectIssues(current_user, projectName):
    fileP = dataString+projectName+'.json'
    filein = open(fileP, 'r')
    #print(fileP)
    #print(filein)
    proj = json.loads(filein.read())
    #print(proj)
    return render_template("issues.html", current_user=current_user,proj=proj)

@app.route('/<current_user>/<projectName>/<Issue_Name>/Active', methods=['GET', 'POST'])
def projectTOCurrentSprint(current_user, projectName, Issue_Name):
    fileP = dataString+projectName+'.json'
    filein = open(fileP, 'r')
    #print(fileP)
    #print(filein)
    proj = json.loads(filein.read())
    #print(proj)
    #print(proj['currentSprint'])
    todList=proj['currentSprint']["TODO"]
    #print(todList)
    for idea in proj['BackLog']:
        if idea['Issue_Name'] == Issue_Name:
            copy=idea # get item based on Issue_Name
            #print(copy)
            todList.append(copy) # copy it to BackLog
            proj['currentSprint']["TODO"]=todList
            proj['BackLog'].remove(copy)  #remove from SandBox
            with open(fileP,'w') as fileout:
                fileout.write(json.dumps(proj, indent=2))
    return redirect(url_for('projectCurrentSprint', current_user=current_user, projectName= proj['name'] ))

@app.route('/<current_user>/<projectName>/SandBox', methods=['GET', 'POST'])
def projectSandBox(current_user, projectName):
    fileP = dataString+projectName+'.json'
    filein = open(fileP, 'r')
    #print(fileP)
    #print(filein)
    proj = json.loads(filein.read())
    #print(proj)
    if request.method == 'POST':
        Issue_Name=request.form["Issue_Name"]
        time=request.form["time"]
        Description=request.form["Description"]
        item={"Issue_Name":Issue_Name,"time":time,"Description":Description,  "Tasks": {
    "TODO": [],
    "In_Progress": [],
    "Done": []
  } }
        proj["SandBox"].append(item)
        with open(fileP,'w') as fileout:
            fileout.write(json.dumps(proj, indent=2))
    form=SandBox()
    form2=ConvertToBackLog()
    return render_template("SandBox.html", current_user=current_user,proj=proj, form=form,form2=form2)


# This Function moves item from sandbox to BackLog
#We will use this as a template for moving item from backlog to Current sprint
#Data:
#current_user: name of user
#projectName: Name of Project being done
#Issue_Name: id and name of idea being moved
#Issue_Name: id and name of idea being moved
@app.route('/<current_user>/<projectName>/<Issue_Name>', methods=['GET', 'POST'])
def SandBoxTOBackLog(current_user, projectName, Issue_Name):
    fileP = dataString+projectName+'.json'
    filein = open(fileP, 'r')
    #print(fileP)
    #print(filein)
    proj = json.loads(filein.read())

    todList = proj['SandBox']
    for idea in todList:
        print(idea['Issue_Name'], file=sys.stdout)
        if idea['Issue_Name'] == Issue_Name:
            copy=idea # get item based on Issue_Name
            print(idea)
            proj['BackLog'].append(idea) # copy it to BackLog
            print(proj["BackLog"], file=sys.stdout)
            proj['SandBox'].remove(idea)  #remove from SandBox
            print(proj["SandBox"], file=sys.stdout)
            with open(fileP,'w') as fileout:
                fileout.write(json.dumps(proj, indent=2))
    return redirect(url_for('projectBackLog', current_user=current_user, projectName= proj['name'] ))

@app.route('/<current_user>/createProject', methods=['GET', 'POST'])
def createProj(current_user):
    form = ProjectForm()
    if request.method == 'POST':
        filein = open(dataString+'projects.json', 'r')
        projList = json.loads(filein.read())
        filein.close()
        #print(projList, file=sys.stdout)

        projectName=request.form["titleOfProject"]
        description=request.form["description"]

        #print(projectName)
        #print(description)
        newProj={"name":projectName,"description":description}
        projList.append(newProj)
        #print(projList)

        with open(dataString+'projects.json','w') as fileout:
            fileout.write(json.dumps(projList, indent=2))


        projectJson = {"name":projectName,"SandBox":list(),"BackLog":list(),"sprints":list(),"currentSprint":dict(),"Discussion":list()}

        with open(dataString+projectName+".json",'w') as jsonfile:
            jsonfile.write(json.dumps(projectJson, indent=2))

        return redirect(url_for('projectList', current_user= current_user))
    return render_template("createProject.html",form=form)

@app.route('/DBTEST')
def dbTest():
    filein = open('C:/Users/swald/group7/app/data/projects.json', 'r')
    #print (filein.read(), file=sys.stdout)
    filein.seek(0,0)
    projList = json.loads(filein.read())
    # #print(projList)
    # db.session.add(p)
    # db.session.commit()
    # ListOProjects = Projects.query.all()
    # for p in ListOProjects:
    #     #print(p.name, p.ProjectID)
    # projList = ListOProjects
    return render_template("projects.html",projectList=projList, current_user=current_user)

@app.route('/logOut')
def logOut():
    current_user=""
    return  redirect(url_for('home'))

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

@app.errorhandler(500)
def not_found(error):
    return render_template('error.html'), 500
