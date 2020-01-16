# Tip calculator based on level of service
###############################################################################
# prompt for total bill amount and service level
bill_total = float(input('What is the bill amount? '))
service_level = input('How was the level of service? (good, fair or bad) ')

if service_level == "good":
    tip = bill_total * .20
elif service_level == "fair":
    tip = bill_total * .15
else:
    tip = bill_total * .10

bill_with_tip = tip + bill_total

print("Tip amount: $" + '%.2f' % tip)
print("Total amount: $" + '%.2f' % bill_with_tip)


###########################################################
# REVISIT TO ADD GROUP ORDER CALCULATION
###########################################################
