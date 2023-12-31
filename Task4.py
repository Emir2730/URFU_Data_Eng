import csv

filename = "text/text_4_var_63"

age_filter = 25 + (63 % 10)

d = {}
csv_del = ","
last_name_first = True

with open(filename, mode = "r", encoding="utf-8") as f:
    l = csv.reader(f, delimiter=csv_del)
    m = 0
    for r in l:
        d.update({r[0] : r[1:-1]})
        m += int(r[4][:-1])

m /= len(d)

ml = dict(sorted([[int(k) , v] for k, v in d.items() if (int(v[-1][:-1]) >= m) and (int(v[2]) > age_filter)]))

with open(filename + "out", mode = "w", encoding="utf-8") as f:
    d_w = csv.writer(f, delimiter=csv_del)
    for item in ml.items():

        if last_name_first == True:
            name = " ".join(item[1][1::-1])
        else:
            name = " ".join(item[1][0:2])

        d_w.writerow([item[0]] + [name, *item[1][2:]])
