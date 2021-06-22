import pandas as pd
import json

def main():

    infile = open("y20data.json", "r")
    line = infile.readline()
    infile.close()
    full = json.loads(line)


    resp = pd.read_csv("resp.csv")
    resp = resp[['roll', 'name', 'email']]

    regd = list()

    for _, row in resp.iterrows():
        roll = row['roll']
        # regd.add(roll)
        if roll in regd:
            print("duplicate entry:", dem)
            print(row)
        regd.append(roll)
        email = (row['email']).strip()
        dem = (full[str(roll)]["u"] + "@iitk.ac.in").strip()
        if dem.lower() != email.lower():
            print("email mismatch:", dem)
            print(row)            
    print(len(regd))
    outfile = open("regd.json", "w")
    outfile.write(json.dumps(list(regd)))
    outfile.close()

if __name__ == '__main__':
    main()
