"""Reproducible illustrative annuity scenarios. Not SSB microdata."""
def monthly_annuity(principal_nok: float, annual_rate_percent: float, years: int) -> float:
    r = annual_rate_percent / 1200
    n = years * 12
    return principal_nok / n if r == 0 else principal_nok * r / (1 - (1 + r) ** (-n))

def household_cashflow(income_nok: float, mortgage_nok: float, years: int, rate_pct: float, essential_costs_monthly: float, income_shock_pct: float = 0):
    monthly_income = income_nok * (1 + income_shock_pct/100) / 12
    repayment = monthly_annuity(mortgage_nok, rate_pct, years)
    return {"payment_nok": round(repayment, 2), "monthly_residual_nok": round(monthly_income - repayment - essential_costs_monthly, 2), "payment_to_disposable_income_pct": round(100 * repayment / monthly_income, 2)}

if __name__ == '__main__':
    print(household_cashflow(720000, 3000000, 25, 5.31, 26000))
