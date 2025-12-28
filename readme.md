# Case study : Pendulum on a cart using LQR

> Here we simulate and animate an inverted pendulum on a cart controlled using Linear Quadratic Regulator(LQR). 

## Table of Contents
- [About](#about)
- [Installation](#installation)
- [Usage](   )
- [Features]()

# About

This is an example from Steve Brunton's Data-book

# Installation

```bash
git clone https://github.com/Imdadullah-Raji/ddse_control.git
cd ddse_control
```

# Usage
 edit and run `lqr_cartpend.py` to generate the csv file containing the trajectory. Then run `cartpend_animations0.py` to visualize.

# Features 
`cartpend.py` models the physics of inverted pendulum on a cart. `lqr_cartpend.py` simulates the control input for stabilizing the pendulum, it generates the control input and also simulates the resulting trajectory of the pendulum, then saves it to `lqr_cartpend_data.csv`
