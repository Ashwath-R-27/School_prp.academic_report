from flask import Flask, render_template, request , url_for
from db import get_db

app = Flask(__name__)



def header_div():
    logo_url=url_for('static', filename='logo.png')
    header=f""" <div class="header">
        <div class="logo"><a href="#"><img src="{logo_url}" id="logo"></a></div>
        <div class="header_content">
            <div class="header_text_1">SVGV MATRICULATION HIGHER SECONDARY SCHOOL</div>
        </div>
    </div>"""
    return header

@app.route("/")
def first():
    header=header_div()
    return render_template("home.html",header_div=header)



@app.route("/HSC_2026")
def hscmark():
    header=header_div()
    return render_template("hscmarkpg.html",header_div=header)

@app.route("/HSC_2026/Marks/Group")
def hscgrpwisemarks():
    header=header_div()
    db=get_db()
    cursor=db.cursor()
    cursor.execute("SELECT DENSE_RANK() OVER (ORDER BY total DESC) AS rank_no, reg_no, class, name, lang, eng, phy, chem, csc, maths, total, cut_off FROM hsc_result_cs")
    data=cursor.fetchall()
    db.close()
    return render_template("hscgrpmark.html",header_div=header,records=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
