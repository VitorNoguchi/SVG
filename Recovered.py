# draw a quarter of a square (symmetry coming)
import csv
from datetime import datetime


class RecoveredCsv:
    def __init__(self):
        print("abrir csv")

    def csv(self):
        color = ['black','yellow', 'red', 'blue', 'green', 'orange', 'purple', 'pink', 'brown', 'grey']
        ctry_list = ['world', 'brazil', 'spain', 'us', 'italy','teste']
        recovered_svg = {'ctry_list': ctry_list, 'ctry_pt': [], 'ctry_len': [], 'dt_pt': [], 'dt_lbl_pt': [], 'dt_lbl_loc': [],
                     'wld_ylbl_loc': [], 'ctry_ylbl_loc': [], 'wld_lbl': [],'ctry_lbl': [], 'color': color}
        recovered = {'wmax': [], 'cmax': [],'dt_lbl': [], 'diff_dt': [], 'dt_count': []}

        for pais in ctry_list:
            dt_lbls = []; ctry = []; dt = []; diff_dt = []; dt_count = []
            try:
                dt_count.append(0)
                with open(f'/home/semantix/PycharmProjects/Desafio4/{pais}.csv','r') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    for row in readCSV:
                        if row[0] != 'Country':
                            ctry.append(row[3].replace('.', ''))
                            dt.append(row[4])
                    csvfile.close()
            except:
                print('arquivo invalido')                            #CRIAR LOG
            if pais == 'world':
                recovered['wmax'].append(ctry[-1])
            else:
                recovered['cmax'].append(ctry[-1])
            for a in range(0, len(dt)):
                b = datetime.strptime(dt[a], '%d/%m/%Y %H:%M') - datetime.strptime(dt[1], '%d/%m/%Y %H:%M')
                e = int(b.total_seconds()/60)
                diff_dt.append(e)
                dt_lbls.append(dt[a].split(' ')[0])

            count = 0
            for w in range(0,len(dt_lbls)-1):
                if dt_lbls[w] == dt_lbls[w+1]:
                    count += 1
                else:
                    count += 1
                    dt_count.append(count)

            dt_lbl = list(dict.fromkeys(dt_lbls))
            recovered_svg['ctry_pt'].append(ctry)
            recovered_svg['dt_pt'].append(dt)
            recovered_svg['dt_lbl_pt'].append(dt_lbl)
            recovered['diff_dt'].append(diff_dt)
            recovered['dt_count'].append(dt_count)

        ymax = max(recovered['cmax'], key=int)
        for w in range(0,len(recovered_svg['ctry_pt'][0])):
            recovered_svg['ctry_pt'][0][w] = (420 - (358 * (int(recovered_svg['ctry_pt'][0][w]) / int(recovered['wmax'][0]))))

        for x in range(1,len(recovered_svg['ctry_pt'])):
            for z in range(0,len(recovered_svg['ctry_pt'][x])):
                recovered_svg['ctry_pt'][x][z] = (420 - 358 * (int(recovered_svg['ctry_pt'][x][z]) / int(ymax)))
        for dd in range(0,len(recovered_svg['dt_pt'])):
            for d in range(0,len(recovered_svg['dt_pt'][dd])):
                recovered_svg['dt_pt'][dd][d] = (615 * (recovered['diff_dt'][dd][d] / recovered['diff_dt'][dd][-1]) + 190)

        if ((int(recovered['wmax'][0]) / 100000) -  (int(int(recovered['wmax'][0]) / 100000))) >= 0.5:
            for wz in range(0, (int(int(recovered['wmax'][0]) / 200000)) + 2):
                recovered_svg['wld_lbl'].append(round(wz*0.2, 1))
                recovered_svg['wld_ylbl_loc'].append(420 - wz * 200000 * (358 / int(recovered['wmax'][0])))
        else:
            for wz in range(0, (int(int(recovered['wmax'][0]) / 200000) + 1)):
                recovered_svg['wld_lbl'].append(round(wz*0.2, 1))
                recovered_svg['wld_ylbl_loc'].append(420 - wz * 200000 * (358 / int(recovered['wmax'][0])))

        if ((int(ymax) / 200000) - int(int(ymax) / 200000)) >= 0.5:
            for cz in range(0, (int(int(ymax) / 20000) + 2)):
                recovered_svg['ctry_lbl'].append(cz*20)
                recovered_svg['ctry_ylbl_loc'].append(420 - cz * 20000 * (358 / int(ymax)))
        else:
            for cz in range(0, (int(int(ymax) / 200000) + 1)):
                recovered_svg['ctry_lbl'].append(cz * 20)
                recovered_svg['ctry_ylbl_loc'].append(420 - cz * 20000 * (358 / int(ymax)))

        for ddl in range(0, len(recovered_svg['dt_pt'])):
            for dl in recovered['dt_count'][ddl]:
                recovered_svg['dt_lbl_loc'].append(recovered_svg['dt_pt'][ddl][dl])
                recovered_svg['dt_lbl_loc'] = list(dict.fromkeys(recovered_svg['dt_lbl_loc']))

        ctry_len = []
        for a in range(0, len(recovered_svg['ctry_list'])):
            ctry_len.append(len(recovered_svg['ctry_pt'][a]))
        recovered_svg['ctry_len'].append(ctry_len)

        return recovered_svg

if __name__ == "__main__":
    a = RecoveredCsv().csv()
