from flask import Flask, flash, redirect, render_template, request, url_for

# configure application
app = Flask(__name__)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response
        
@app.route("/", methods=["GET", "POST"])
def home():
    """render home screen."""
    if request.method == "POST":
         # Ensure proper usage
        if request.form.get("CurrentGPA") == "" or request.form.get("CurrentGPA") == None or str.isalpha(request.form.get("CurrentGPA")):  
            return render_template("Templates/error.html", message = "Enter Current GPA as a Number")
        if request.form.get("DesiredGPA") == "" or request.form.get("DesiredGPA") == None or str.isalpha(request.form.get("DesiredGPA")):    
            return render_template("Templates/error.html", message = "Enter Desired GPA as a Number")
        if request.form.get("Classes") == "" or request.form.get("Classes") == None or str.isalpha(request.form.get("Classes")):  
            return render_template("Templates/error.html", message = "Enter Desired Classes as Number")
        if request.form.get("AssumedGrade") == "" or request.form.get("AssumedGrade") == None:
            return render_template("Templates/error.html", message = "Enter Assumed Grade for Class")
            
        classes = float(request.form.get("Classes"))
        curGPA = float(request.form.get("CurrentGPA"))
        desGPA = float(request.form.get("DesiredGPA"))
        grade = request.form.get("AssumedGrade")
        print(grade)
        weight = 0
        
        if grade == "A":
            weight = 4.0
        elif grade == "A-":
            weight = 3.67
        elif grade == "B+":
            weight = 3.33
        elif grade == "B":
            weight = 3.0
        elif grade == "B-":
            weight  = 2.67
        elif grade == "C+":
            weight = 2.33
        elif grade == "C":
            weight = 2.0
        elif grade == "C-":
            weight = 1.67
        elif grade == "D+":
            weight = 1.33
        elif grade == "D":
            weight = 1.0
        elif grade == "F":
            weight = 0
        else:
            return render_template("Templates/error.html", message = "Enter a vaild grade")
        
        print(weight)
        
        gpa = curGPA
        totake = 0
        
        if weight  < desGPA:
            return render_template("Templates/error.html", message = "Desired GPA is higher than Assumed Grade. Please enter a higher assumed grade.")
        
        while gpa < desGPA:
            totake += 1
            gpa = float((curGPA * classes) + (weight * totake))
            gpa = float(gpa/(classes + totake))
        
        
        return render_template("Templates/results.html", grade = grade, GPA = desGPA, totake = totake)
        
        
    else:
        return render_template("Templates/home.html")
    
@app.route("/error")
def error():
    """render error message."""
    return render_template("Templates/error.html", message = "")
    
@app.route("/results")
def results():
    """render results"""
    return render_template("Templates/results.html")