import pandas as pd
import json
import random


def fulldata():
    infile = open("y20data.json", "r")
    line = infile.readline()
    infile.close()
    return json.loads(line)


def regdroll():
    infile = open("regd.json", "r")
    line = infile.readline()
    infile.close()
    return json.loads(line)


def makepair(a, b, data, c):
    dt1 = data[str(a)]
    dt2 = data[str(b)]
    sa1 = "Mr." if dt1["g"] == "M" else "Ms."
    sa2 = "Mr." if dt2["g"] == "M" else "Ms."
    if dt1["g"] != dt2["g"]:
        c[0] = c[0]+1
    elif dt2["g"] == "M":
        c[1] = c[1]+1
    else:
        c[2] = c[2]+1
    data = {'re_em' : [dt1["u"]+"@iitk.ac.in", dt2["u"]+"@iitk.ac.in"],
            're_sa': [sa1, sa2],
            're_name': [dt1["n"], dt2["n"]],
            'pe_sa' : [sa2, sa1],
            'pe_name': [dt2["n"], dt1["n"]],
            'pe_r': [b, a],
            'pe_u': [dt2["u"]+"@iitk.ac.in", dt1["u"]+"@iitk.ac.in"],
            }
    df = pd.DataFrame(data)
    df.to_csv("email2.csv",index=False, header=False, mode="a")


def init():
    data = {'re_em': [],
            're_sa': [],
            're_name': [],
            'pe_sa': [],
            'pe_name': [],
            'pe_r': [],
            'pe_u': [],
            }
    df = pd.DataFrame(data)
    df.to_csv("email2.csv", index=False)

def main():
    regd = regdroll()
    full = fulldata()
    count = [0, 0, 0]
    init()
    while(len(regd)>1):
        a = random.choice(regd)
        regd.remove(a)
        b = random.choice(regd)
        regd.remove(b)
        makepair(a, b, full, count)
    print(regd)
    print(count)
    print("M: ", count[0] + count[1]*2)
    print("F: ", count[0] + count[2]*2)
if __name__ == '__main__':
    main()
