import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Black-Scholes Formula
def black_scholes(S, K, T, r, sigma, option_type="call"):
    d1 = (np.log(S / K) + (r + (sigma ** 2) / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option_type == "call":
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")
    
    return price

# Sensitivity Analysis Visualization
def plot_option_sensitivity(S, K, T, r, sigma_range):
    call_prices = []
    put_prices = []
    for sigma in sigma_range:
        call_prices.append(black_scholes(S, K, T, r, sigma, "call"))
        put_prices.append(black_scholes(S, K, T, r, sigma, "put"))
    
    plt.figure(figsize=(10, 6))
    plt.plot(sigma_range, call_prices, label="Call Option Price")
    plt.plot(sigma_range, put_prices, label="Put Option Price")
    plt.xlabel("Volatility (σ)")
    plt.ylabel("Option Price")
    plt.title("Option Pricing Sensitivity to Volatility")
    plt.legend()
    plt.grid()
    plt.show()

# Main Execution
if __name__ == "__main__":
    S = float(input("Enter stock price (S): "))
    K = float(input("Enter strike price (K): "))
    T = float(input("Enter time to maturity in years (T): "))
    r = float(input("Enter risk-free interest rate (r): "))
    
    sigma_range = np.linspace(0.1, 1.0, 50)  # Volatility range from 10% to 100%
    plot_option_sensitivity(S, K, T, r, sigma_range)
