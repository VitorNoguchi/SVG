# draw a quarter of a square (symmetry coming)
import csv
from datetime import datetime


class RecoveredCsv:
    def __init__(self):
        print("abrir csv")

    def csv(self):
        corona_cases = {'wld_pt': [], 'br_pt': [], 'sp_pt': [], 'us_pt': [], 'it_pt': [], 'dt_pt': [], 'dt_lbl_pt': [],
                        'dt_lbl_loc': [], 'wld_ylbl_loc': [], 'ctry_ylbl_loc': [], 'wld_lbl': [],'ctry_lbl': []}

        wld = []; br = []; sp = []; us = []; it = []; dt = []; diff_dt = []; dt_count = [0]

        for pais in ['world', 'brazil', 'spain', 'us', 'italy']:
            with open(f'/home/semantix/PycharmProjects/Desafio4/{pais}.csv','r') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                for row in readCSV:
                    if row[0] != 'Country':
                        if pais == 'world':
                            wld.append(row[3].replace('.', ''))
                        elif pais == 'brazil':
                            br.append(row[3].replace('.',''))
                            dt.append(row[4])
                        elif pais == 'spain':
                            sp.append(row[3].replace('.', ''))
                        elif pais == 'us':
                            us.append(row[3].replace('.', ''))
                        else:
                            it.append(row[3].replace('.', ''))
                csvfile.close()


        for a in range(0, len(dt)):
            b = datetime.strptime(dt[a], '%d/%m/%Y %H:%M') - datetime.strptime(dt[0], '%d/%m/%Y %H:%M')
            e = int(b.total_seconds()/60)
            diff_dt.append(e)
            corona_cases['dt_lbl_pt'].append(dt[a].split(' ')[0])

        count = 0

        for w in range(0,len(corona_cases['dt_lbl_pt'])-1):
            if corona_cases['dt_lbl_pt'][w] == corona_cases['dt_lbl_pt'][w+1]:
                count += 1
            else:
                count += 1
                dt_count.append(count)

        corona_cases['dt_lbl_pt']= list(dict.fromkeys(corona_cases['dt_lbl_pt']))
        ymax = max(int(us[-1]), int(it[-1]), int(sp[-1]), int(br[-1]), key=int)

        for x in range(0,len(br)):
            corona_cases['wld_pt'].append(420 - 358 * (int(wld[x]) / int(wld[-1])))
            corona_cases['br_pt'].append(420 - 358 * (int(br[x]) / int(ymax)))
            corona_cases['sp_pt'].append(420 - 358 * (int(sp[x]) / int(ymax)))
            corona_cases['us_pt'].append(420 - 358 * (int(us[x]) / int(ymax)))
            corona_cases['it_pt'].append(420 - 358 * (int(it[x]) / int(ymax)))
            corona_cases['dt_pt'].append(615 * (diff_dt[x]/diff_dt[-1]) + 190)

        if (int(wld[-1]) / 100000) - int(int(wld[-1]) / 100000) >= 0.5:
            for wz in range(1, (int(int(wld[-1]) / 200000) + 2)):
                corona_cases['wld_lbl'].append(wz*200)
                corona_cases['wld_ylbl_loc'].append(420 - wz * 200000 * (358 / int(wld[-1])))
        else:
            for wz in range(1, (int(int(wld[-1]) / 200000) + 1)):
                corona_cases['wld_lbl'].append(wz * 200)
                corona_cases['wld_ylbl_loc'].append(420 - wz * 200000 * (358 / int(wld[-1])))
        if ((int(ymax) / 200000) - int(int(ymax) / 200000)) >= 0.5:
            for cz in range(1, (int(int(ymax) / 20000) + 1)):
                corona_cases['ctry_lbl'].append(cz*20)
                corona_cases['ctry_ylbl_loc'].append(420 - cz * 20000 * (358 / int(ymax)))
        else:
            for cz in range(1, (int(int(ymax) / 200000) + 1 )):
                corona_cases['ctry_lbl'].append(cz*20)
                corona_cases['ctry_ylbl_loc'].append(420 - cz * 20000 * (358 / int(ymax)))
        for dl in dt_count:
            corona_cases['dt_lbl_loc'].append(corona_cases['dt_pt'][dl])

        print()
        return corona_cases

if __name__ == "__main__":
    a = RecoveredCsv().csv()
