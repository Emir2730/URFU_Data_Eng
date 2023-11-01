filename = "text/text_2_var_63"
det = ","

with open(filename) as f:
    lines = f.readlines()

with open(filename + "out", "w") as f:
    for l in lines:
        f.write(f"{sum(map(int, l.strip().split(det)))}\n")
       

