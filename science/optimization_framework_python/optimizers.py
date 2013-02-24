#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2013 Jérémie DECOCK (http://www.jdhp.org)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import warnings

class Optimizer:

    def plotSamples(self, x, y):

        assert y.shape[1]==1

        if x.shape[1]==1:
            # 1D case
            plt.plot(x[:,0], y, ".")
            
            x_min = x[y.argmin(), :]
            y_min = y.min()
            plt.plot(x_min, y_min, ".r")

            plt.show()
        elif x.shape[1]==2:
            # 2D case
            fig = plt.figure()
            ax = axes3d.Axes3D(fig)
            ax.scatter(x[:,0], x[:,1], y, color='b')
            
            x_min = x[y.argmin(), :]
            y_min = y.min()
            ax.scatter(x_min[0], x_min[1],  y_min, color='r')

            plt.show()
        else:
            warnings.warn("Cannot plot samples: too many dimensions.")

    def plotCosts(self, y):

        assert y.shape[1]==1

        plt.plot(y)
        plt.show()


# OPTIMIZERS ##################################################################

class NaiveMinimizer(Optimizer):
    
    def optimize(self, objective_function, num_samples=1000):

        dmin = objective_function.domain_min
        dmax = objective_function.domain_max
        
        x_samples = np.random.uniform(dmin, dmax, [num_samples, objective_function.ndim])
        y_samples = objective_function(x_samples)
        x_min = x_samples[y_samples.argmin(), :]

        self.plotSamples(x_samples, y_samples)
        self.plotCosts(y_samples)

        return x_min


class GradientDescent(Optimizer):

    def __init__(self, delta):
        self.delta = delta

    def optimize(self, objective_function, num_samples=1000):

        dmin = objective_function.domain_min
        dmax = objective_function.domain_max
        
        x = np.random.uniform(dmin, dmax, objective_function.ndim)

        x_samples = np.zeros([num_samples, objective_function.ndim])

        # Compute the gradient of objective_function at x
        for sample_index in range(num_samples):
            nabla = np.zeros(objective_function.ndim)
            for dim_index in range(objective_function.ndim):
                delta_vec = np.zeros(objective_function.ndim)
                delta_vec[dim_index] = self.delta

                y1 = objective_function(x - delta_vec)
                y2 = objective_function(x + delta_vec)

                nabla[dim_index] = y2 - y1

            x = x - nabla

            # Keep an history of x to plot things...
            x_samples[sample_index, :] = x

        y_samples = objective_function(x_samples)
        self.plotSamples(x_samples, y_samples)
        self.plotCosts(y_samples)

        return x

