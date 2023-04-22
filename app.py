from flask import Flask,request,render_template
app = Flask(__name__)
app.secret_key="secret"
@app.route("/",methods=['POST','GET']) 
def index():
   
 return render_template("index.html") 

@app.route("/submit",methods=['POST','GET'])  
def submit(): 
   
   if request.method=="POST": 
      error = "Both grade and credit fields must be either filled or empty."
      g1=str(request.form['input_g1'])
      c1=(request.form['input_c1'])
      g2=str(request.form['input_g2'])
      c2=(request.form['input_c2'])
      g3=str(request.form['input_g3'])
      c3=(request.form['input_c3'])
      g4=str(request.form['input_g4'])
      c4=(request.form['input_c4'])
      g5=str(request.form['input_g5'])
      c5=(request.form['input_c5'])
      g6=str(request.form['input_g6'])
      c6=(request.form['input_c6'])
      g7=str(request.form['input_g7'])
      c7=(request.form['input_c7'])
      g8=str(request.form['input_g8'])
      c8=(request.form['input_c8'])
      g9=str(request.form['input_g9'])
      c9=(request.form['input_c9'])
      g10=str(request.form['input_g10'])
      c10=(request.form['input_c10'])
      g11=str(request.form['input_g11'])
      c11=(request.form['input_c11'])
      g12=str(request.form['input_g12'])
      c12=(request.form['input_c12'])
      try:
       c1 = float(c1) if c1 != "" else 0
       c2 = float(c2) if c2 != "" else 0
       c3 = float(c3) if c3 != "" else 0
       c4 = float(c4) if c4 != "" else 0
       c5= float(c5) if c5 != "" else 0
       c6= float(c6) if c6 != "" else 0
       c7 = float(c7) if c7 != "" else 0
       c8 = float(c8) if c8 != "" else 0
       c9 = float(c9) if c9 != "" else 0
       c10 = float(c10) if c10 != "" else 0
       c11 = float(c11) if c11 != "" else 0
       c12 = float(c12) if c12 != "" else 0
      
      #checking for error conditions
      
       for i in range(1,13):
        g = str(request.form[f"input_g{i}"])
        c = str(request.form[f"input_c{i}"])
        if (g == "" and c != "") or (g != "" and c == ""):
           return render_template("error.html", error=error)

       g1=conversion(g1)
       g2=conversion(g2)
       g3=conversion(g3)
       g4=conversion(g4)
       g5=conversion(g5)
       g6=conversion(g6)
       g7=conversion(g7)
       g8=conversion(g8)
       g9=conversion(g9)
       g10=conversion(g10)
       g11=conversion(g11)
       g12=conversion(g12)
      except Exception as e:
         return render_template("error.html", error=error)
   error = "Both grade and credit fields must be either filled or empty."
   try:
    r=(g1*c1)+(g2*c2)+(g3*c3)+(g4*c4)+(g5*c5)+(g6*c6)+(g7*c7)+(g8*c8)+(g9*c9)+(g10*c10)+(g11*c11)+(g12*c12)
    s=c1+c2+c3+c4+c5+c6+c7+c8+c9+10+c11+c12
    sgpa=(r/s)
    format_float = "{:.2f}".format(sgpa)
    print("credits",c1,c2,c3,c4,c5,c6,c7,c8,"Grades",g1,g2,g3,g4,g5,g6,g7,g8)
    print("SGPA",format_float)
   except Exception as e:
    return render_template("error.html", error=error)
 
  
   return render_template("result.html",result=format_float)
def conversion(g):
    grade_map = {"O": 10, "A+": 9, "A": 8, "B+": 7, "B": 6, "C": 5, "F": 0, "": 0}
    return grade_map.get(g, 0)

@app.errorhandler(404)
def not_found_error(error):
   return render_template('error.html', error=error), 404         
   
if __name__=="__main__":
   app.run(debug=True)   


