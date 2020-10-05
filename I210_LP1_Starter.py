import donation

# main



# Section 1 - get all of the donations and output the values

# As an example of how to get an amount, this gets 1 donation and prints it out
# Run the program a few times and notice that the amount changes.
# If the code won't run, did you put this file and donation.py in the same directory?



#used the for loop fuction to iterate 200 times based on imported file name: donation.py. After that,
#I have set the new variable which is "amount", and it contains 200 random variables those are range in 1 - 20
#used append function to put selected variable into "donation_lst"
donation_lst = []

for i in range(200):
    amount = donation.get_donation()
    donation_lst.append(amount)

print("The donation amounts: ")
print(donation_lst)
print()
print("The donations in order: ")
print(sorted(donation_lst))

print() #-to put enter#



# Section 2 - Compute basic categories


#Starting with setting new 3 variables and those are all set with "0" to start counting the each string in donation_lst
count_small = 0
count_med = 0
count_large = 0

#using a for loop function to iterate until the number of the variables are all founded based on the if, elif, else function.    
for i in donation_lst:
    if i <= 5:
        count_small += 1
    elif i <= 15:
        count_med += 1
    else:
        count_large += 1

print("There were", count_small, "small donations ($5 or less).")
print("There were", count_med, "medium donations ($6 - $15).")
print("There were", count_large, "large donations ($16 or more).")

print() #-to put enter#


# Section 3 - Compute success or failure


#Stratight forward to show how the str and int are combined and printed out#
#Also used the "if" and "else" to show how the statements are showing up depends on the total amount of money#
print("The total amount of money raised is:","$",sum(donation_lst))
if sum(donation_lst) >= 2016:
    print("The fundraising goal was met!")
else:
    print("The fundraising goal was not met.")

print()


# Section 4 - What can you expect from the bank?


#used len function to figure out the length of the sentence starts with "The bank...." because as it shown in the overview pic. the number of letters and dashes are same, so I was trying to make it equal#
cash_out = int(len("The bank cashed this amount out as:"))

print("The bank cashed this amount out as:")
print("-" * cash_out)


#I have named the sum of donation_lst as "total_amount"#
#and then I have named the the number of bills as name of the appropriate president for each actual dollars. for example, Franklin's face is actually printed on $100#
#and then I have calculated the number of dollars by dividing the sum of donation and subtract from the previous total_amount to the previous president#
#and finally print it out with just name of each president.#

total_amount = sum(donation_lst)
franklin = int(total_amount/100)
total_amount1 = (total_amount - franklin*100)
jackson = int(total_amount1/20)
total_amount2 = (total_amount1 - jackson*20)
hamilton = int(total_amount2/10)
total_amount3 = (total_amount2 - hamilton * 10)
lincoln = int(total_amount3/5)
total_amount4 = (total_amount3 - lincoln * 5)
washington = int(total_amount4/1)
total_amount5 = (total_amount4 - washington * 1)

print("$100 bills:", franklin)
print("$20 bills:", jackson)
print("$10 bills:", hamilton)
print("$5 bills:", lincoln)
print("$1 bills:", washington)



