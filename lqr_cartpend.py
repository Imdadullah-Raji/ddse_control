import control
import numpy as np
from cartpend import cartpend
from scipy.integrate import odeint 
import matplotlib.pyplot as plt

def lqr_cartpend(m, M, L, g, d, Q, R):
    """
    outputs the LQR gain matrix K for cart-pendulum system
   
    """

    #linearized  state-space matrices around the upright position
    A = np.array( [[0,1,0,0],
                   [0,-d/M,m*g/M,0],
                   [0,0,0,1],
                   [0, -d/(M*L), -(m+M)*g/(M*L),0]] )
    B = np.array( [[0],
                   [1/M],
                   [0],
                   [1/(M*L)] ] )
    
    #LQR controller gain
    K = control.lqr(A,B,Q,R)[0]

    return K


if __name__ == "__main__":
    #trial parameters 
    m = 1
    M = 5
    L = 2
    g = -10
    d = 1

    # weight matrices 
    Q = np.eye(4) #state cost
    R = 0.001 #control cost

    K = lqr_cartpend(m, M, L, g, d, Q, R)

    print("LQR Gain K: ", K)

    t_span = np.arange(0, 10, 0.0001)
    x0 = np.array([-1, 0, np.pi + 0.1, 0]) #initial state
    x_ref = np.array([1, 0, np.pi, 0]) #reference state
    u = lambda x: -K @ (x - x_ref)
    x = odeint(cartpend, x0, t_span, args=(u, m, M, L, g, d) )

    print("Final state: ", x[-1])

    #plot results 

    fig, ax = plt.subplots( 2,1, figsize=(8,6))
    ax[0].plot(t_span, x[:,0], label='Cart Position')
    ax[0].axhline(x_ref[0], color='r', linestyle='--', label='Reference Position')
    ax[0].set_ylabel('Position (m)')
    ax[0].legend()
    ax[0].grid()
    ax[1].plot(t_span, x[:,2], label='Pendulum Angle')
    ax[1].axhline(x_ref[2], color='r', linestyle='--', label='Reference Angle')
    ax[1].set_ylabel('Angle (rad)')
    ax[1].set_xlabel('Time (s)')
    ax[1].legend()
    ax[1].grid()
    plt.tight_layout()
    plt.show()





