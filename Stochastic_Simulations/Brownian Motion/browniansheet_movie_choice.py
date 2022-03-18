#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    python_simulations.browniansheet_Mult
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This is a simulation for Brownian Sheet....

    A simulation of a Brownian sheet though two different methods.

    1. BrownianSheetWalsh defines the Brownian Sheet through a recursive technique...
    ... using the fact that \int_{[t, t+dt]}\int_{[x, x+dt]} dW(t, x) ~ N(0, dt * dx).

    2. BrownianSheetDaprato uses the expansion given in example 4.9 from DaPrato...
    ... "Stochastic Equations in Infinite Dimensions" on page 88.

    3. BM will simulate multiple standard Brownian paths.

    :copyright: (c) 2022 by Nick Eisenberg <nickeisenberg@gmail.com>.
    :license: LICENSE_NAME, see LICENSE for more details.
    :created at Wed 02 Mar 2022 10:55:11 AM CST
"""

import numpy as np
import matplotlib.pyplot as plt
# import time
import math
from mpl_toolkits.mplot3d.axes3d import Axes3D


def BrownianSheetWalsh(t, nt, x, nx):
    """TODO: Docstring for BrownianSheet.
    :1: TODO
    :returns: TODO
    """
    delta_t = t / nt
    delta_x = x / nx
    # Create the Brownian sheet noise
    W_tx = np.zeros((nx + 1, nt + 1))
    for x in range(nx):
        for t in range(nt):
            dW = np.sqrt(delta_t * delta_x) * np.random.normal(0, 1, size=1)
            W_tx[x + 1, t + 1] = W_tx[x, t + 1] + W_tx[x + 1, t] - W_tx[x, t] + dW[0]
    return W_tx


def BrownianSheetDaprato(t, nt, x, nx, K, t_axis, x_axis):
    delta_t = t / nt
    # delta_x = x / nx
    # Generate K + 1 Brownian Motions simulations.
    # Simulate nt + 1 points: W(t_0) = 0, W(t_1), ..., W(t_k), ..., W(t_n).
    W = np.zeros((nt + 1, K + 1), dtype=float)
    for i in range(K + 1):
        dW = np.sqrt(delta_t) * np.random.normal(0, 1, size=nt)
        W[1:, i] = np.cumsum(dW)

    # Write a function Wtx(t, x) = SUM where SUM is the sum from Example 4.9 DaPrato

    def Wtx(t, x):
        # x_index = int(x / delta_x)
        t_index = int(t / delta_t)
        Bnt = W[t_index]
        sin_in = np.zeros(K + 1)
        frac = np.zeros(K + 1)
        for i in range(K + 1):
            sin_in[i] = (i + .5) * x
            frac[i] = 1 / (i + 1 / 2)
        sin = np.sin(sin_in)
        BSfrac = np.multiply(np.multiply(sin, Bnt), frac)
        sumand = math.sqrt(2 / math.pi) * BSfrac
        return np.sum(sumand)

    # Store the values a matrix (aij) where aij = W( t_j, x_i)
    # Note that a0j = 0 and ai0 = 0 from the definion of the SUM from Example 4.9

    W_tx = np.zeros((nx + 1, nt + 1))

    for i in range(nx + 1):
        for j in range(nt + 1):
            W_tx[i][j] = Wtx(t_axis[j], x_axis[i])
    return W_tx


def BrownianSheetMovie(method):
    # Set K for the case of DaPrato.
    # Note that we must have 0 < x < pi for the case of Daprato. See Example 4.9 - DaPrato.
    K = 40
    # Set the time and space intervals. Choose number of partitions of each.
    # Time
    t = 5
    nt = 100

    # Space
    x = math.pi
    nx = 100

    # create the time and spatial axis
    t_axis = np.linspace(0.0, t, nt + 1)
    x_axis = np.linspace(0.0, x, nx + 1)

    # Plot the Brownian Sheet
    ts, xs = np.meshgrid(t_axis, x_axis)

    fig = plt.figure(figsize=(8, 8))
    # plt.ion()
    plt.show(block=False)
    for i in range(10):
        # Compute the Brownian Sheet
        ax = fig.add_subplot(111, projection='3d')
        # ax = Axes3D(fig, auto_add_to_figure=False)
        fig.add_axes(ax)
        # ax.set_xlabel('$ 0 \\leq t \\leq {} $'.format(t), fontsize=14)
        # ax.set_ylabel('$0 \\leq x \\leq \\pi$', fontsize=14)
        ax.set_title('Brownian Sheet', fontsize=20)
        # Choose either BrownianSheetWalsh or BrownianSheetDaprato
        if method == "DaPrato":
            W_tx = BrownianSheetDaprato(t, nt, x, nx, K, t_axis, x_axis)
        else:
            W_tx = BrownianSheetWalsh(t, nt, x, nx)
        ax.plot_surface(ts, xs, W_tx, rstride=1, cstride=1, cmap='plasma')
        plt.draw()
        plt.pause(0.1)
        plt.clf()
        # time.sleep(1)


def BM():
    # Set the time and space intervals. Choose number of partitions of each.
    # Time
    t = 100
    nt = 2000

    # create the time and spatial axis
    t_axis = np.linspace(0.0, t, nt + 1)
    plt.figure()
    # plt.ion()
    plt.show(block=False)
    for i in range(50):
        plt.title('Standard Brownian motion', fontsize=20)
        dW = np.sqrt(t / nt) * np.random.normal(0, 1, size=nt)
        BM = np.zeros(nt+1)
        BM[1:nt+1] = np.cumsum(dW)
        plt.plot(t_axis, BM)
    plt.show()


if __name__ == "__main__":
    ans = True
    while ans:
        print("""
        1. Simulation via Da Prato's representation.
        2. Simulation via Walsh's Brownian Sheet.
        3. Brownian motion.
        4. Exit/Quit
        """)
        ans = input("What would you like to do? ")
        if ans == "1":
            BrownianSheetMovie("DaPrato")
        elif ans == "2":
            BrownianSheetMovie("Walsh")
        elif ans == "3":
            BM()
        elif ans == "4":
            print("\n Goodbye~!")
            exit(1)
        elif ans != "":
            print("\n Not Valid Choice Try again")
