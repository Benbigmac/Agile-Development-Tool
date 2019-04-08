from flask import render_template, flash, redirect, url_for, request,session
from app import app
from app.forms import LoginForm, RegistrationForm, ProjectForm,TaskForm,SandBox,ConvertToBackLog
import json, sys

current_user=""
#dataString='/Users/lzhou/Documents/group7/app/data/'
dataString='C:/Users/benma/Desktop/cs442/code/group7/app/data/'
#dataString='C:/Users/swald/group7/app/data/'
@app.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()
    if request.method == 'POST':
        current_user=request.form["username"]
        return redirect(url_for('projectList'),current_user=current_user)
    else:
        return render_template("index.html",title="FireScrum",form=form,current_user="")

@app.route('/signUp')
def signUpPage():
    form = RegistrationForm()
    return render_template("signUp.html",form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        current_user=request.form["username"]
        #if current_user.is_authenticated():
        #    g.user = current_user.username
        return redirect(url_for('projectList', current_user= current_user))
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
    print(fileP)
    print(filein)
    proj = json.loads(filein.read())
    print(proj)
    return render_template("accountSettings.html", current_user=current_user,proj=proj)

@app.route('/<current_user>/<projectName>/CurrentSprint')
def projectCurrentSprint(current_user, projectName):
    fileP = dataString+projectName+'.json'
    filein = open(fileP, 'r')
    print(fileP)
    print(filein)
    proj = json.loads(filein.read())
    print(proj)
    return render_template("currentSprint.html", current_user=current_user,proj=proj)

@app.route('/<current_user>/<projectName>/CreateTask')
def projectcreateTask(current_user, projectName):
    fileP = dataString+projectName+'.json'
    filein = open(fileP, 'r')
    print(fileP)
    print(filein)
    proj = json.loads(filein.read())
    print(proj)
    form=TaskForm()
    return render_template("CreateTask.html", current_user=current_user,proj=proj,form=form)

@app.route('/<current_user>/<projectName>/Sprints')
def projectSprints(current_user, projectName):
    fileP = dataString+projectName+'.json'
    filein = open(fileP, 'r')
    print(fileP)
    print(filein)
    proj = json.loads(filein.read())
    print(proj)
    return render_template("sprints.html", current_user=current_user,proj=proj)

@app.route('/<current_user>/<projectName>/Discussion')
def talkBox(current_user, projectName):
    fileP = dataString+projectName+'.json'
    filein = open(fileP, 'r')
    print(fileP)
    print(filein)
    proj = json.loads(filein.read())
    print(proj)
    return render_template("discussionBoard.html", current_user=current_user,proj=proj)

@app.route('/<current_user>/projects')
def projectList(current_user):
    filein = open((dataString+'projects.json'), 'r')
    print (filein.read(), file=sys.stdout)
    filein.seek(0,0)
    projList = json.loads(filein.read())
    return render_template("projects.html",projectList=projList, current_user=current_user)

@app.route('/<current_user>/<projectName>')
def projectSplash(current_user, projectName):
    fileP = dataString+projectName+'.json'
    filein = open(fileP, 'r')
    print(fileP)
    print(filein)
    proj = json.loads(filein.read())
    print(proj)
    return render_template("projectDash.html", current_user=current_user,proj=proj)

@app.route('/<current_user>/<projectName>/BackLog')
def projectBackLog(current_user, projectName):
    fileP = dataString+projectName+'.json'
    filein = open(fileP, 'r')
    print(fileP)
    print(filein)
    proj = json.loads(filein.read())
    print(proj)
    return render_template("backlog.html", current_user=current_user,proj=proj)

@app.route('/<current_user>/<projectName>/SandBox', methods=['GET', 'POST'])
def projectSandBox(current_user, projectName):
    fileP = dataString+projectName+'.json'
    filein = open(fileP, 'r')
    print(fileP)
    print(filein)
    proj = json.loads(filein.read())
    print(proj)
    if request.method == 'POST':
        Issue_Name=request.form["Issue_Name"]
        time=request.form["time"]
        Description=request.form["Description"]
        item={"Issue_Name":Issue_Name,"time":time,"Description":Description}
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
    print(fileP)
    print(filein)
    proj = json.loads(filein.read())
    print(proj)
        #sandList
    for idea in proj['SandBox']:
        if idea['Issue_Name'] == Issue_Name:
            copy=idea # get item based on Issue_Name
            print(copy)
            proj['BackLog'].append(copy) # copy it to BackLog
            proj['SandBox'].remove(copy)  #remove from SandBox
            with open(fileP,'w') as fileout:
                fileout.write(json.dumps(proj, indent=2))
    return redirect(url_for('projectBackLog', current_user=current_user, projectName= proj['name'] ))

    #return render_template("SandBox.html", current_user=current_user,proj=proj, form=form, form2=form2)

@app.route('/<current_user>/createProject', methods=['GET', 'POST'])
def createProj(current_user):
    form = ProjectForm()
    if request.method == 'POST':
        filein = open(dataString+'projects.json', 'r')
        projList = json.loads(filein.read())
        filein.close()
        print(projList, file=sys.stdout)

        projectName=request.form["titleOfProject"]
        description=request.form["description"]

        print(projectName)
        print(description)
        newProj={"name":projectName,"description":description}
        projList.append(newProj)
        print(projList)

        with open(dataString+'projects.json','w') as fileout:
            fileout.write(json.dumps(projList, indent=2))

        return redirect(url_for('projectList', current_user= current_user))
    return render_template("createProject.html",form=form)

@app.route('/DBTEST')
def dbTest():
    filein = open('C:/Users/swald/group7/app/data/projects.json', 'r')
    print (filein.read(), file=sys.stdout)
    filein.seek(0,0)
    projList = json.loads(filein.read())
    # print(projList)
    # db.session.add(p)
    # db.session.commit()
    # ListOProjects = Projects.query.all()
    # for p in ListOProjects:
    #     print(p.name, p.ProjectID)
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
