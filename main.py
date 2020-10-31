import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

def upperBound(l) :
  # Your code for determing the other end of the confidence limit based on the 
  # value of the lower bound for this region goes here.
  
  

# You should not need to modify anything from here onwards
xvals = np.linspace(-2.32,2.32,100)
yvals = upperBound( xvals )
plt.plot( xvals, yvals, 'k-')
plt.savefig("confidence_limit.png")
