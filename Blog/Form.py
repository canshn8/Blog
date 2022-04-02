from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt
from functools import wraps
from flask import flash





#Kullanıcı Giriş Decarator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "login_success" in session:
            return f(*args, **kwargs)
        else:
            flash("Bu Sayfayı Görüntülemek İçin Lütfen Giriş Yapınız","warning")
            return redirect(url_for("login"))
    return wrap
#MySQL ile Veritabanı Kurulumları
#Kayıt Olma
class RegisterForm(Form):

    name = StringField("İsim Soyisim:",validators=[validators.length(min=2,max=25,message="Burası Boş Bırakılamaz")])
    username =  StringField("Kullanıcı Adı:",validators=[validators.length(min=2,max=15,message="Burası Boş Bırakılamaz")])
    email = StringField("Email",validators=[validators.email(message="Lütfen Geçerli Bir Email Adresi Girin:")])
    password = PasswordField("Parola:",validators=[
        validators.DataRequired(message="Lütfen Geçerli Parola Giriniz:"),
        validators.EqualTo(fieldname ="confirm" ,message="Parola Uyuşmuyor:")
    ])
    confirm = PasswordField("Parola Doğrula:")
#Giriş Yap

class LoginForm(Form):
    username = StringField("Kullanıcı Adı:")
    password = PasswordField("Parola:")
   
app = Flask(__name__)
app.secret_key ="site"

app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "site"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

#Giriş İndexi
@app.route("/")
def home():
    return render_template("index.html")

#AnaSayfa İndexi
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/Duyuru")
def duyuru():
    return render_template("duyuru.html")


#Python Bölümü
@app.route("/Python")
def Python():
    return render_template("Python/python.html")

@app.route("/Python-Os")
def os():
    return render_template("Python/os_py.html")

@app.route("/Python-Numpy")
def numpy():
    return render_template("Python/numpy_py.html")

@app.route("/Python-Range")
def range():
    return render_template("Python/range_py.html")

@app.route("/Python-Request")
def requestt():
    return render_template("Python/request_py.html")

@app.route("/Python-Tkinter")
def tkinter():
    return render_template("Python/tkinter_py.html")

@app.route("/Python-PyWin32")
def pywin32():
    return render_template("Python/pywin32_py.html")
#Python Bitiş



#C# Giriş 
@app.route("/CSharp")
def CSharp():
    return render_template("CSharp/CSharp.html")

@app.route("/CSharp-OPP")
def opp():
    return render_template("CSharp/OPP.html")

@app.route("/CSharp-Multithread")
def Multithread():
    return render_template("CSharp/Multithread.html")




#JavaScript Giriş
@app.route("/JavaScript")
def JavaScript():
    return render_template("JavaScript/JavaScript.html")



@app.route("/JavaScript-React")
def react():
    return render_template("JavaScript/React.html")

@app.route("/JavaScript-Angular")
def angular():
    return render_template("JavaScript/Angular.html")

@app.route("/JavaScript-Ember")
def ember():
    return render_template("JavaScript/Ember.html")

@app.route("/JavaScript-SPA")
def spa():
    return render_template("JavaScript/SPA.html")

@app.route("/JavaScript-VirtualDom")
def virtualdom():
    return render_template("JavaScript/virtualdom.html")

@app.route("/JavaScript-Meteor")
def meteor():
    return render_template("JavaScript/meteor.html")

@app.route("/JavaScript-VUE")
def vue():
    return render_template("JavaScript/vue.html")


@app.route("/JavaScript-TypeScript")
def typescript():
    return render_template("JavaScript/typescript.html")

@app.route("/JavaScript-NodeJs-Kurulumu") 
def nodejs():
    return render_template("JavaScript/NodeJs.html")
#JavaScript Bitiş



#Css 'e Giriş
@app.route("/Css")
def css():
    return render_template("Css/css.html")

@app.route("/Css-Bootstrap")
def bootstrap():
    return render_template("Css/bootstrap.html")

@app.route("/Css-Foundation")
def foundation():
    return render_template("Css/foundation.html")

@app.route("/Css-Animate")
def animate():
    return render_template("Css/animate.html")

@app.route("/Css-Semantic")
def semantic():
    return render_template("Css/semantic.html")

@app.route("/Css-UIKit")
def uıkit():
    return render_template("Css/uıkit.html")
#Css Bitiş



#Html 'e Giriş

@app.route("/Html")
def html():
    return render_template("Html/html.html")

#Html Bitiş



#Harici Konular
@app.route("/BootstrapNavbar")
def navbar():
    return render_template("navbar.html")

@app.route("/Diller-Ne-İşe-Yarar")
def diller():
    return render_template("diller.html")

@app.route("/Temel-Seviye-Css")
def TemelSeviyeCss():
    return render_template("TemelSeviyeCss.html")

@app.route("/Temel-Seviye-Html")
def TemelSeviyeHtml():
    return render_template("TemelSeviyeHtml.html")

@app.route("/Temel-Seviye-JavaScript")
def TemelSeviyeJavaScript():
    return render_template("TemelSeviyeJavaScript.html")

@app.route("/BackEnd")
def backend():
    return render_template("backend.html")

@app.route("/FrontEnd")
def frontend():
    return render_template("frontend.html")






#Kayıt Ol
@app.route("/register",methods=["GET","POST"])
def register():
    form = RegisterForm(request.form)

    if request.method == "POST" and form.validate():
    

        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(form.password.data)

        cursor = mysql.connection.cursor()

        sorgu = "Insert into users(name,username,email,password) VALUES(%s,%s,%s,%s)"

        cursor.execute(sorgu,(name,username,email,password))

        mysql.connection.commit()
        cursor.close()

        flash("Hesabınızı Kontrol Etmek İçin Lütfen Giriş Yapınız!  ","warning")

        return redirect(url_for("login"))

    else:
        return render_template("register.html",form = form)


#Giriş Yap

@app.route("/login",methods=["GET","POST"])
def login():
    form = LoginForm(request.form)

    if request.method == "POST":
        
        username = form.username.data
        password_entered = form.password.data
        
        cursor = mysql.connection.cursor()

        sorgu = "Select * From  users where username  = %s"
        result = cursor.execute(sorgu,(username,))

        if result > 0:
            data = cursor.fetchone()
            real_password = data["password"]

            if sha256_crypt.verify(password_entered,real_password):
                flash("Başarıyla Giriş Yaptınız","success")
                session["login_success"] = True
                session["username"] = username 
                

                return redirect(url_for("home"))
            else:
                flash("Sistemde Böyle Bir Parola Bulunmamaktadaır!","danger")
                return redirect(url_for("login"))

        else:
            flash("Böyle Bir Kullanıcı Yok ","danger")
            return redirect(url_for("login"))

    return render_template("login.html",form = form)

 



#Çıkış Yap
@app.route("/logoff")
def logoff()
    session.clear()
    return redirect("home")



if __name__ =="__main__":
    app.run(debug =True)

