# Print the last item of gdp_cap and life_exp
print(gdp_cap[-1])
print(life_exp[-1])


# Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis
plt.plot(gdp_cap,life_exp)
    
# Display the plot
plt.show()

# Change the line plot below to a scatter plot
plt.plot(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.scatter(gdp_cap,life_exp)
plt.xscale('log')
# Show plot
plt.show()


# Import package

import matplotlib.pyplot as plt

# Build Scatter plot
plt.scatter(pop,life_exp)


# Show plot
plt.show()