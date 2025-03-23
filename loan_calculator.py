def get_loan_principal():
    loan_principal = int(input("Enter loan principal amount: "))
    return loan_principal

def calculate_loan_interest(principal, interest_rate):
    interest = interest_rate * principal / 100  # Convert percentage to decimal
    return interest

def get_loan_term():
    loan_term_years = int(input("Enter loan term in years: "))
    loan_term_months = loan_term_years * 12
    return loan_term_months

def get_monthly_payment():
    pay_per_month = float(input("Enter monthly payment amount: "))
    return pay_per_month

def calculate_payoff_period(principal, interest_rate, monthly_payment):
    # Simple payoff calculation (this is a basic version)
    # For a more accurate calculation, you would need to account for compounding interest
    monthly_interest_rate = interest_rate / 100 / 12

    if monthly_payment <= principal * monthly_interest_rate:
        return "Your monthly payment is too small to pay off the loan"

    months = 0
    balance = principal

    while balance > 0:
        interest = balance * monthly_interest_rate
        balance = balance + interest - monthly_payment
        months += 1

    years = months / 12
    payoff_time = f"It will take you {years:.2f} years to pay off the loan"
    return payoff_time

# Get user inputs
principal = get_loan_principal()
interest_rate = float(input("Enter loan interest rate (%): "))
monthly_payment = get_monthly_payment()

# Calculate and display result
payoff_result = calculate_payoff_period(principal, interest_rate, monthly_payment)
print(payoff_result)
