

from flask import *
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("layout.html")

#------------------------------------------CAPITALIZE-------------------------------------------------------------------

@app.route("/capitalize")
def capitalize_template():
    return render_template("capitalize.html")


@app.route("/capitalize",methods=["POST"])
def capitalize():
    str1=request.form['str1']
    result=str1.capitalize()
    return render_template("capitalize.html",result=result)

 #_---------------------------------------------UPPER CASE-----------------------------------------------------------------------
@app.route("/uppercase")
def uppercase_template():
    return render_template("uppercase.html")

@app.route("/uppercase",methods=["POST"])
def uppercase():
    str1=request.form["str1"]
    result=str1.upper()
    return render_template("uppercase.html",result=result)

#------------------------------------------------LOWERCASE-------------------------------------------------------------------------

@app.route("/lowercase")
def lowercase_template():
    return render_template("lowercase.html")

@app.route("/lowercase",methods=["POST"])
def lowercase():
    str1=request.form["str1"]
    result=str1.lower()
    return render_template("lowercase.html",result=result)

#--------------------------------------------------compare two strings--------------------------------------------------------------

@app.route("/compare")
def compare_template():
    return render_template("compare.html")

@app.route("/compare",methods=["POST"])
def compare():
    str1=request.form["str1"]
    str2=request.form["str2"]
    str3=str1.lower()
    str4=str2.lower()
    if str1==str2 and str3==str4:
        return render_template("compare.html",letter_wise="Strings are equal",meaning_wise="Strings are equal")
    elif str1!=str2 and str3==str4:
        return render_template("compare.html",letter_wise=" Strings are not equal",meaning_wise="Strings are equal")
    elif str1!=str2 and str3!=str4:
        return render_template("compare.html",letter_wise="Strings are not equal", meaning_wise="Strings ar not equal")


#--------------------------------------------------------------------concatenate-------------------------------------------
@app.route("/concatenate")
def concatenate_template():
    return render_template("concatenate.html")

@app.route("/concatenate",methods=["POST"])
def concatenate():
    str1=request.form["str1"]
    str2=request.form["str2"]
    result=str1+ " "+ str2
    return render_template("concatenate.html",result=result)


#---------------------------------------------------------------reverse-----------------------------------------------------------

@ app.route("/reverse")
def reverse_template():
    return render_template("/reverse.html")

@app.route("/reverse",methods=["POST"])
def reverse():
    str1=request.form["str1"]
    result=str1[::-1]

    str1=str1.split(" ")[::-1]
    result2=" ".join(str1)

    return render_template("reverse.html",result=result,result2=result2)

#---------------------------------------------------------------Length of the string----------------------------------------------------

@app.route("/length")
def length_template():
    return render_template("/length.html")

@app.route('/length',methods=["POST"])
def length():
    string=request.form["str1"]
    length1=len(string)
    length2=len([i for i in string if i.isalpha()])
    length3=len([i for i in string if i.isnumeric()])
    length4=len(string.strip().split(" "))
    return render_template("length.html",length1=length1,length2=length2,length3=length3,length4=length4)



#----------------------------------------------------------Slicing-------------------------------------------------

@app.route('/slicing')
def slicing_template():
    return render_template("slicing.html")

@app.route("/slicing",methods=["POST"])
def slicing():
    str=request.form["str"]
    start=int(request.form["start"])
    end=int(request.form["end"])
    steps=int(request.form["steps"])
    sliced_str=str[start:end:steps]
    print(str)
    print(start)

    return render_template("slicing.html",sliced_str=sliced_str)

#---------------------------------------------------------------replace---------------------------------------------------------------------------

@app.route("/replace")
def replacing_template():
    return render_template("replace.html")

@app.route("/replace",methods=["POST"])
def replacing():
    str1=request.form["str"]
    replace_str1=request.form["replace_str1"]
    replace_str2=request.form["replace_str2"]
    
    replaced_str=str1.replace(replace_str1,replace_str2)
    return render_template("replace.html",replaced_str=replaced_str)









if __name__=="__main__":
    app.run(debug=True)
