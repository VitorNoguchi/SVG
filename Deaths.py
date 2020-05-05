# draw a quarter of a square (symmetry coming)
import csv
from datetime import datetime


class DeathsCsv:
    def __init__(self):
        print("abrir csv")

    def csv(self):
        color = ['black','yellow', 'red', 'blue', 'green', 'orange', 'purple', 'pink', 'brown', 'grey']
        ctry_list = ['world', 'brazil', 'spain', 'us', 'italy','teste']
        deaths_svg = {'ctry_list': ctry_list, 'ctry_pt': [], 'ctry_len': [], 'dt_pt': [], 'dt_lbl_pt': [], 'dt_lbl_loc': [],
                     'wld_ylbl_loc': [], 'ctry_ylbl_loc': [], 'wld_lbl': [],'ctry_lbl': [], 'color': color}
        deaths = {'wmax': [], 'cmax': [],'dt_lbl': [], 'diff_dt': [], 'dt_count': []}

        for pais in ctry_list:
            dt_lbls = []; ctry = []; dt = []; diff_dt = []; dt_count = []
            try:
                dt_count.append(0)
                with open(f'/home/semantix/PycharmProjects/Desafio4/{pais}.csv','r') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    for row in readCSV:
                        if row[0] != 'Country':
                            ctry.append(row[2].replace('.', ''))
                            dt.append(row[4])
                    csvfile.close()
            except:
                print('arquivo invalido')                            #CRIAR LOG
            if pais == 'world':
                deaths['wmax'].append(ctry[-1])
            else:
                deaths['cmax'].append(ctry[-1])
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
            deaths_svg['ctry_pt'].append(ctry)
            deaths_svg['dt_pt'].append(dt)
            deaths_svg['dt_lbl_pt'].append(dt_lbl)
            deaths['diff_dt'].append(diff_dt)
            deaths['dt_count'].append(dt_count)

        ymax = max(deaths['cmax'], key=int)
        for w in range(0,len(deaths_svg['ctry_pt'][0])):
            deaths_svg['ctry_pt'][0][w] = (420 - (358 * (int(deaths_svg['ctry_pt'][0][w]) / int(deaths['wmax'][0]))))

        for x in range(1,len(deaths_svg['ctry_pt'])):
            for z in range(0,len(deaths_svg['ctry_pt'][x])):
                deaths_svg['ctry_pt'][x][z] = (420 - 358 * (int(deaths_svg['ctry_pt'][x][z]) / int(ymax)))
        for dd in range(0,len(deaths_svg['dt_pt'])):
            for d in range(0,len(deaths_svg['dt_pt'][dd])):
                deaths_svg['dt_pt'][dd][d] = (615 * (deaths['diff_dt'][dd][d] / deaths['diff_dt'][dd][-1]) + 190)

        if ((int(deaths['wmax'][0]) / 1000000) - (int(int(deaths['wmax'][0]) / 1000000))) >= 0.5:
            for wz in range(0, (int(int(deaths['wmax'][0]) / 50000)) + 2):
                deaths_svg['wld_lbl'].append(wz*50)
                deaths_svg['wld_ylbl_loc'].append(420 - wz * 50000 * (358 / int(deaths['wmax'][0])))
        else:
            for wz in range(0, (int(int(deaths['wmax'][0]) / 50000) + 1)):
                deaths_svg['wld_lbl'].append(wz*50)
                deaths_svg['wld_ylbl_loc'].append(420 - wz * 50000 * (358 / int(deaths['wmax'][0])))

        if ((int(ymax) / 200000) - int(int(ymax) / 10000)) >= 0.5:
            for cz in range(0, (int(int(ymax) / 10000) + 2)):
                deaths_svg['ctry_lbl'].append(cz*10)
                deaths_svg['ctry_ylbl_loc'].append(420 - cz * 10000 * (358 / int(ymax)))
        else:
            for cz in range(0, (int(int(ymax) / 10000) + 1)):
                deaths_svg['ctry_lbl'].append(cz * 10)
                deaths_svg['ctry_ylbl_loc'].append(420 - cz * 10000 * (358 / int(ymax)))

        for ddl in range(0, len(deaths_svg['dt_pt'])):
            for dl in deaths['dt_count'][ddl]:
                deaths_svg['dt_lbl_loc'].append(deaths_svg['dt_pt'][ddl][dl])
                deaths_svg['dt_lbl_loc'] = list(dict.fromkeys(deaths_svg['dt_lbl_loc']))

        ctry_len = []
        for a in range(0, len(deaths_svg['ctry_list'])):
            ctry_len.append(len(deaths_svg['ctry_pt'][a]))
        deaths_svg['ctry_len'].append(ctry_len)

        return deaths_svg

if __name__ == "__main__":
    a = DeathsCsv().csv()
