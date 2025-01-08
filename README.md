# Black Scholes Option Pricing Simulator

## Overview

The **Black-Scholes Option Pricing Simulator** is a Python-based simulator that calculates option prices using the **Black-Scholes model**. It provides a visual representation of how option prices (both call and put) are affected by volatility. The tool is designed for financial professionals, traders, and students to explore the effects of different parameters on option pricing.

## Features

- **Black-Scholes Formula**: Calculate the price of European call and put options.
- **Sensitivity Analysis**: Visualize how option prices change with varying volatility.
- **Interactive Input**: Enter stock price, strike price, time to maturity, and risk-free interest rate.
- **Visualization**: Graphically plot call and put option prices against volatility.

## Requirements

Before running the tool, make sure you have Python 3.x installed along with the required libraries:

- `numpy`: For numerical calculations.
- `matplotlib`: For plotting the option price sensitivity.
- `scipy`: For statistical functions like the cumulative distribution function (CDF).

Install the necessary Python libraries by running:

```bash
pip install numpy matplotlib scipy
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/BlackScholesOptionPricingSimulator.git
   cd BlackScholesOptionPricingSimulator
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Python script:

   ```bash
   python main.py
   ```

2. Input the required values when prompted:
   - Stock price (S)
   - Strike price (K)
   - Time to maturity in years (T)
   - Risk-free interest rate (r)

3. The tool will calculate the option prices for call and put options and display a graph showing the sensitivity of option prices to varying volatility.

## File Structure

```
BlackScholesOptionPricingSimulator/
│
├── main.py       # Main script for option pricing and visualization
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

By: Adithya Sai Srinivas
