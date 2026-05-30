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

def hscgroups():
    db=get_db()
    cursor=db.cursor()
    cursor.execute("SELECT groupname,groupcode FROM hsc_groups")
    groups=cursor.fetchall()
    cursor.execute("SELECT head_1,head_2,head_3,head_4 FROM hsc_groups")
    grpheads=cursor.fetchall()
    grpdtls=[]
    grpdtls.append(groups)
    grpdtls.append(grpheads)
    db.close()
    return grpdtls

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
    datas=[]
    header=header_div()
    db=get_db()
    grpdtls=hscgroups()
    groups=grpdtls[0]
    grpheads=grpdtls[1]
    cursor=db.cursor()
    for i in range(0,len(groups)):
        cursor.execute(f"SELECT DENSE_RANK() OVER (ORDER BY total DESC) AS rank_no, reg_no, class, name, lang, eng, phy, chem, {groups[i][1]}, maths, total, cut_off FROM hsc_result_{groups[i][1]}")
        data=cursor.fetchall()
        datas.append(data)
    db.close()
    return render_template("hscgrpmark.html",header_div=header,records=datas,groups=groups,grpheads=grpheads,length=len(groups))


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
