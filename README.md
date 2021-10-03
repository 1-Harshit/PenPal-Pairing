# PenPal-Pairing

**Jun'22 PenPal Pairing Algo and script**  
---



This was used for automated paring of PenPal initiative [Website Link](https://home.iitk.ac.in/~harshitr20/penpal/)

## How to use this:

1. Download the google form response as `.csv` and update `resp.csv`   
   Make sure you have feild heading as `'roll', 'name', 'email'`
2. Run `validate.py` this will make a list of all rolls in resposne and update you about email mismatch and duplicate entries.
3. Then you'll see `regd.json`.
4. Now, Run `pair.py`. This will create an emaling list. of ramdomised pair
5. Use template `template.html` and email using mailmerge, with 5 second gap.
5. Run `mailinglist.py` to make list of all emails for further broadcast.

## Contact
In case you face any isuue executing feel free to [contact Me](https://home.iitk.ac.in/~harshitr20#contact) (Harshit Raj BT/BS Y20 Senator, Students' Senate).

Other Core Team member: 
- Shreya Agarwal and Somya Gupta, BT/BS Y20 Senator, Students' Senate
