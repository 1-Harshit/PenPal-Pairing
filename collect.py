import json


def main():
    infile = open("/home/salazar/data.json", "r")
    line = infile.readline()
    infile.close()
    full = json.loads(line)
    final = dict()
    for entry in full:
        try:
            roll = int(entry["i"])
        except:
            continue
        if roll < 200000 or roll > 202000:
            continue
        ok = dict()
        ok["n"] = entry["n"]
        ok["u"] = entry["u"]
        ok["d"] = entry["d"]
        ok["g"] = entry["g"]
        ok["p"] = entry["p"]
        ok["pr"] = 0
        final[roll] = ok
    
    outfile = open("y20data2.json", "w")
    outfile.write(json.dumps(final))
    
if __name__ == '__main__':
    main()