from scipy.optimize import root_scalar

# A farmer buys a dairy cow for 120,000 KES.
# Yearly net income from milk (KES) over 5 years, then the cow is sold.
cash_flows = [-120000, 30000, 36000, 40000, 40000, 65000]

def npv(rate):
    return sum(cf / (1 + rate)**t for t, cf in enumerate(cash_flows))

def d_npv(rate):
    return sum(-t * cf / (1 + rate)**(t + 1)
               for t, cf in enumerate(cash_flows) if t > 0)

newton = root_scalar(npv, fprime=d_npv, x0=0.10, method="newton", xtol=1e-12)
secant = root_scalar(npv, x0=0.05, x1=0.30, method="secant", xtol=1e-12)

print(f"IRR using Newton-Raphson: {newton.root:.4%}")
print(f"IRR using Secant method: {secant.root:.4%}")
print(f"NPV at Newton solution: {npv(newton.root):.6f}")
print("Newton iterations:", newton.iterations)
print("Secant iterations:", secant.iterations)

bank_rate = 0.12
print(f"NPV at a {bank_rate:.0%} bank rate: {npv(bank_rate):.2f} KES")