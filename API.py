#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template
import Cases
import Deaths
import Recovered

CS = Cases.CasesCsv()
dth = Deaths.DeathsCsv()
rcv = Recovered.RecoveredCsv()
app = Flask(__name__)

@app.route('/cases', methods=['GET', 'POST'])
def foo():
    cs_dataa = CS.csv()
    ctry_len = []
    for a in range(0,len(cs_dataa['ctry_list'])):
        ctry_len.append(len(cs_dataa['ctry_pt'][a]))
    return render_template('cases.html', dic= cs_dataa, ctry_count= len(cs_dataa['ctry_list']), ctry_len= ctry_len,
                           wld_lbl_len = len(cs_dataa['wld_lbl']), ctry_lbl_len = len(cs_dataa['ctry_lbl']),
                           dt_lbl_len= len(cs_dataa['dt_lbl_loc']))

@app.route('/deaths', methods=['GET', 'POST'])
def foo1():
    dth_data = dth.csv()
    ctry_len = []
    for a in range(0,len(dth_data['ctry_list'])):
        ctry_len.append(len(dth_data['ctry_pt'][a]))
    return render_template('deaths.html', dic= dth_data, ctry_count= len(dth_data['ctry_list']), ctry_len= ctry_len,
                           wld_lbl_len = len(dth_data['wld_lbl']), ctry_lbl_len = len(dth_data['ctry_lbl']),
                           dt_lbl_len= len(dth_data['dt_lbl_loc']))

@app.route('/recovered', methods=['GET', 'POST'])
def foo2():
    rcv_data = rcv.csv()
    ctry_len = []
    for a in range(0,len(rcv_data['ctry_list'])):
        ctry_len.append(len(rcv_data['ctry_pt'][a]))
    return render_template('recovered.html', dic= rcv_data, ctry_count= len(rcv_data['ctry_list']), ctry_len= ctry_len,
                           wld_lbl_len = len(rcv_data['wld_lbl']), ctry_lbl_len = len(rcv_data['ctry_lbl']),
                           dt_lbl_len= len(rcv_data['dt_lbl_loc']))

if __name__ == '__main__':
    app.run(debug=True)

