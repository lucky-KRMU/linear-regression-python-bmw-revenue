

## 📊 Project Overview
The script processes historical revenue data for BMW (2006–2025) to determine the growth trend. By transforming the years into a centered time series (where $\sum X = 0$), it simplifies the linear regression calculation to predict future financial performance.

### The Linear Equation
The script solves for the trend line equation:
$$y = a + bx$$

Where:
*   **$y$**: Predicted Revenue (Billion Euros)
*   **$a$**: The Y-intercept (mean revenue when the centered year is zero)
*   **$b$**: The slope (average annual growth rate)
*   **$x$**: The time deviation from the calculated mid-point

---

## 🛠️ Code Functionality

### 1. Data Preparation
The script utilizes two primary datasets:
*   `bmw_year`: A list of years from 2006 to 2025.
*   `bmw_revenue`: Corresponding revenue in billion euros for those years.

### 2. Time Centering
To simplify calculations, the script calculates a `mid_term`. Since the dataset contains 20 entries (an even number), the midpoint is the average of the two middle years ($2015.5$).
The years are then transformed into $X$ values by subtracting this midpoint, ensuring the sum of $X$ is zero.

### 3. Statistical Calculations
The script calculates the following parameters:
*   **$\sum Y$**: Sum of all revenues.
*   **$\sum XY$**: Sum of the product of centered years and revenue.
*   **$\sum X^2$**: Sum of the squares of centered years.

### 4. Revenue Prediction
Using the derived constants $a$ and $b$, the script calculates the expected revenue for **2026** by determining its distance from the midpoint:
$$x = 2026 - 2015.5 = 10.5$$

---

## 🚀 How to Use
1.  Ensure you have **Python 3.x** installed.
2.  Copy the script into a file named `main.py`.
3.  Run the script:
    ```bash
    python main.py
    ```
4.  The console will output the trend equation and the specific revenue forecast for 2026.

---

## 📈 Key Formulae Used
Because the data is centered ($\sum X = 0$), the standard regression formulas are simplified:

*   **Intercept ($a$):**
    $$a = \frac{\sum Y}{n}$$
*   **Slope ($b$):**
    $$b = \frac{\sum XY}{\sum X^2}$$

---

## 📝 Note on Data
The script includes a commented-out section for a "5-year short-term analysis." You can toggle between the long-term trend (20 years) and short-term trend (5 years) by commenting/uncommenting the respective `bmw_revenue` and `bmw_year` blocks.
```