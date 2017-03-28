##Program to produce plots showing different orders of growth

import pylab, math

def showGrowth(lower, upper):
    log = []
    linear = []
    quadratic = []
    logLinear = []
    exponential = []
    for n in range(lower, upper+1):
        log.append(math.log(n, 2)) #log order of growth
        linear.append(n) # linear order of growth
        logLinear.append(n*math.log(n, 2)) #log linear order of growth
        quadratic.append(n**2) # quadratic order of growth
        exponential.append(2**n) #exponential order of growth
    pylab.plot(log, label = 'log')
    pylab.plot(linear, label = 'linear')
    pylab.legend(loc = 'upper left')
    pylab.figure()
    pylab.plot(linear, label = 'linear')
    pylab.plot(logLinear, label = 'log linear')
    pylab.legend(loc = 'upper left')
    pylab.figure()
    pylab.plot(logLinear, label = 'log linear')
    pylab.plot(quadratic, label = 'quadratic')
    pylab.legend(loc = 'upper left')
    pylab.figure()
    pylab.plot(quadratic, label = 'quadratic')
    pylab.plot(exponential, label = 'exponential')
    pylab.legend(loc = 'upper left')
    pylab.figure()
    pylab.plot(quadratic, label = 'quadratic')
    pylab.plot(exponential, label = 'exponential')
    pylab.semilogy()
    pylab.legend(loc = 'upper left')
    return

showGrowth(1, 1000)
pylab.show()
    
    
        
