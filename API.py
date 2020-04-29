#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template
import Cases
import Deaths
import Recovered
import cs

CS = Cases.CasesCsv()
dth = Deaths.DeathsCsv()
rcv = Recovered.RecoveredCsv()
cases_par = cs.CasesCsv()
app = Flask(__name__)

@app.route('/cases', methods=['GET', 'POST'])
def foo():
    cs_data = CS.csv()
    return render_template('cases.html', dic_cs= cs_data, len_cs=len(cs_data['br_pt']), world_label_len_cs = len(cs_data['wld_lbl']),
                           country_label_len_cs = len(cs_data['ctry_lbl']), dates_label_len_cs= len(cs_data['dt_lbl_loc']))

@app.route('/deaths', methods=['GET', 'POST'])
def foo1():
    dth_data = dth.csv()
    return render_template('deaths.html', dic_dth= dth_data, len_dth=len(dth_data['br_pt']), world_label_len_dth = len(dth_data['wld_lbl']),
                           country_label_len_dth = len(dth_data['ctry_lbl']), dates_label_len_dth= len(dth_data['dt_lbl_loc']))

@app.route('/recovered', methods=['GET', 'POST'])
def foo2():
    rcv_data = rcv.csv()
    return render_template('recovered.html', dic= rcv_data, len=len(rcv_data['br_pt']), world_label_len = len(rcv_data['wld_lbl']),
                           country_label_len = len(rcv_data['ctry_lbl']), dates_label_len= len(rcv_data['dt_lbl_loc']))

@app.route('/', methods=['GET', 'POST'])
def foo3():
    cs_dataa = cases_par.csv()
    return render_template('cases2.html', dic= cs_dataa, ctry_count= len(cs_dataa['ctry_list']), ctry_len= cs_dataa['ctry_len'],
                           wld_lbl_len = len(cs_dataa['wld_lbl']), ctry_lbl_len = len(cs_dataa['ctry_lbl']),
                           dt_lbl_len= len(cs_dataa['dt_lbl_loc']))

if __name__ == '__main__':
    app.run(debug=True)

