from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import random, hashlib, os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
app.config["SECRET_KEY"]=os.getenv("SECRET_KEY")


app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("MYSQL_LINK")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


courses = {
   "CS-201": "Discrete Mathematical Structures",
   "CS-203": "Data Structures and Algorithms",
   "CS-207": "Data Base and Information System",
   "CS-303": "Operating Systems",
   "CS-305": "Computer Architecture",
   "CS-307": "Optimisation Algorithms and Techniques",
   "CS-309": "Parallel Computing",
   "CS-403": "Machine Learning",
   "CS-411": "Advanced Algorithms",
   "CS-412": "Pattern Recognition",
   "CS-417": "Cryptography and Network Security",
   "CS-418": "Systems and Usable Security",
   "CS-419": "Computer Vision"
   }


class Student(db.Model):
   userid = db.Column(db.String(50), primary_key = True)
   first_name = db.Column(db.String(100), nullable = False)
   last_name = db.Column(db.String(100), nullable = False)
   mobile = db.Column(db.String(10), nullable = False)
   password = db.Column(db.String(500), nullable = False)
   course_list = db.Column(db.String(30), nullable = False)

   def __init__(self, userid, first_name, last_name, mobile, password, course_list):
      self.userid = userid
      self.first_name = first_name
      self.last_name = last_name
      self.mobile = mobile
      self.password = password
      self.course_list = course_list


class Courses(db.Model):
   course_id = db.Column(db.String(6), primary_key = True)
   course = db.Column(db.String(100), unique = True, nullable = False)

   def __init__(self, course_id, course):
      self.course_id = course_id
      self.course = course

# db.create_all()


# for key in courses:
#    db.session.add(Courses(key, courses[key]))
# db.session.commit()


@app.route('/register/', methods=["POST", "GET"])
def register_page():
   if request.method == 'POST':
      usermail = request.form['usermail']
      first_name = request.form['fname']
      last_name = request.form['lname']
      mobile = request.form['mobile']
      password = request.form['password']
      cpassword = request.form['cpassword']
      encryptedPassword = hashlib.sha1(password.encode()).hexdigest()
      course_list = (" ").join(random.sample(courses.keys(), random.randint(2, 4)))

      storedUserId = Student.query.filter_by(userid = usermail).first()
      if storedUserId:
         return render_template("register.html", registererror = "is-invalid", first_name = first_name, last_name = last_name, mobile = mobile, password = password, cpassword = cpassword)
      else:
         db.session.add(Student(usermail, first_name, last_name, mobile, encryptedPassword, course_list ))
         db.session.commit()
         session["username"] = usermail
         return redirect(url_for('profile_page', username = usermail))
   return render_template("register.html", registererror = "")


@app.route('/login/', methods=["POST", "GET"])
def login_page():
   if request.method == 'POST':
      usermail = request.form['usermail']
      password = request.form['password']
      storedUserId = Student.query.filter_by(userid = usermail).first()
      if storedUserId:
         if storedUserId.password == hashlib.sha1(password.encode()).hexdigest():
            session["username"] = usermail
            return redirect(url_for('profile_page', username = usermail))
         else:
            return render_template("login.html", loginerror = "is-invalid", errormsg = "Incorrect Password, try again")
      else:
         return render_template("login.html", loginerror = "is-invalid", errormsg = "Invalid User ID, try again" )
   return render_template("login.html", loginerror = "")


@app.route('/profile/<username>')
def profile_page(username):
   if "username" in session:
      if session["username"] == username:
         storedUserId = Student.query.filter_by(userid = username).first()
         course_list = storedUserId.course_list.split()
         courses = Courses.query.all()
         course_dict = {}
         for i in course_list:
            for j in courses:
               if i == j.course_id:
                  course_dict[i] = j.course
         return render_template("profile.html", name = storedUserId.first_name, course_dict = course_dict)
   flash("login first!")
   return redirect("/login")


@app.route("/logout")
def logout():
   if "username" in session:
      session.pop("username", None)
      return redirect("/login")
   else:
      flash("login first!")
      return redirect("/login")


if __name__ == '__main__':
   app.run()
