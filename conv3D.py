import numpy as np
from math import *
from settings import *

def conv3D(x,y):
    h_ = h[0]
    r_ = r[0]
    theta_ = theta[0]

    shift_y = (r_**2 + h_**2) / r_ * 0.25

    C = 1 - (h_**2/2 + r_**2/2) / (r_**2 + h_**2 - x*r_*cos(theta_) - y*r_*sin(theta_))
    proj_x = x + C*(r_*cos(theta_) - x)
    proj_y = y + C*(r_*sin(theta_) - y)
    proj_z = C*h_

    P_x = (r_**2 + h_**2) / (4*r_) * cos(theta_)
    P_y = (r_**2 + h_**2) / (4*r_) * sin(theta_)
    P_z = 0

    u = [r_*cos(theta_)/2-P_x, r_*sin(theta_)/2-P_y, h_/2]
    v = [-sin(theta_), cos(theta_), 0]
    PA = [proj_x - P_x, proj_y - P_y, proj_z - P_z]

    conv_x = np.dot(PA,v)
    conv_y = np.dot(PA,u) / sqrt(np.dot(u,u))

    return (15*conv_x + WIDTH//2, HEIGHT//2 - 15*(conv_y - shift_y))