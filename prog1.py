def calculate_compound_interest(principal,rate,time):
    """
    Calculate the compound interest.

    :param prinicpal: The inital amount of money (float or int).
    :param rate: The annual interest rate (float or int).
    :param time: The number of periods the money is invested for (float or int).
    :return: The compound interest (float).
    """

    #convert rate from percentage to decimal

    rate_deci = rate/100

    #cal compound interest

    amount = principal *(1 + rate_deci)** time
    compound_interest = amount - principal

    return compound_interest

#input values
principal = float(input("enter principal value"))
rate = float (input("enter anuual rate in percentage"))
time = float (input("enter the time period"))

#cal comp interest

interest = calculate_compound_interest(principal,rate,time)


#output result

print(f"the compound interest is: {interest:2f}")


















