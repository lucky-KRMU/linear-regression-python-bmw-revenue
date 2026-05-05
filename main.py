# initial variables
a=b=0
x=0

Y_values = []
X_values = []

#Data
bmw_revenue = [
    49.01, 56.02, 53.20, 50.68, 60.48,
    68.82, 76.85, 76.06, 80.40, 92.18,
    94.16, 98.68, 97.48, 104.21, 98.99,
    111.24, 142.61, 155.50, 142.38, 
    133.45
]

bmw_year = [2006, 2007, 2008, 2009, 2010, 2011, 
            2012, 2013, 2014, 2015, 2016, 2017, 
            2018, 2019, 2020, 2021, 2022, 2023,
            2024, 2025
            ]



# Initializing the values
Y_values = bmw_revenue
X_values = bmw_year



# finding out the value of n
n = len(X_values)
print(n)
# making the values of X
mid_term = 0

if n%2 == 0:
    mid_term = (X_values[int(n//2)-1] + X_values[(int(n//2))]) / 2
else:
    mid_term = X_values[int(n//2)]


X_values = [(x-mid_term) for x in X_values]

print(mid_term)
print(X_values, sum(X_values))




# Required Parameters
sigma_y = sum(Y_values)
sigma_x = sum(X_values)

sigma_xy = sum([x*y for x,y in zip(X_values, Y_values)])
sigma_s_sqrt = sum([x**2 for x in X_values])



# Finding the actual values

# Since the value of sigmaX = 0
# b = ((n*sigma_xy)-(sigma_x*sigma_y))/((n*sigma_s_sqrt)-(sigma_x**2))
# a = (sigma_y-(b*sigma_x))/n

# The updated formula
b = sigma_xy/sigma_s_sqrt
a = sigma_y/n



# the main equation
y = a + (b * x)


print(f"y = {a} + {b}x")



print(n,sigma_x, sigma_y, sigma_xy)


# Now finding the expected sales for the year 2026

x = 2026 - mid_term
y = a + (b * x)

print(f"The expected sales for the year 2026 is {y} Billion Euroes")

