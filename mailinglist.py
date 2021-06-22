import pandas as pd

def main():
    mail = pd.read_csv("final.csv")
    mail = mail[['re_em', 're_name']]
    
    infile = open("mails.txt", "a")
    infile.write(', '.join(' {} <{}>'.format(entry['re_name'], entry['re_em']) for _, entry in mail.iterrows()))



if __name__ == '__main__':
    main()
