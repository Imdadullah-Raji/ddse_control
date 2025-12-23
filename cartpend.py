import numpy as np


def cartpend( x, t,  u, m, M, L, g, d):
    """
     x: state of the pendulum: pos x[0], vel x[1], pendulum angle x[2], angular velocity x[3]
     u: control input (force applied to cart)
     m: mass of the pendulum
     M: mass of the cart
     L: Length of the pendulum
     g: gravitational acceleartion
     d: damping coefficient
    """

    dxdt = np.zeros(4)
    u = u(x)

    #how the state changes over time
    dxdt[0] = x[1]
    dxdt[1] = (-m*m*L*L*g*np.sin(x[2])*np.cos(x[2]) 
               +m*L*L*(m*L*x[3]*x[3]*np.sin(x[2])-d*x[1])+m*L*L*u)/(m*L*L*(M+m*(1-np.cos(x[2])*np.cos(x[2]))))
    dxdt[2] = x[3]
    dxdt[3] = ( (m+M)*m*g*L*np.sin(x[2]) - m*L*np.cos(x[2])*
                (m*L*x[3]*x[3]*np.sin(x[2])-d*x[1]+u) )/( m*L*L*( M+m*(1-np.cos(x[2])**2) ) )
                
    return dxdt