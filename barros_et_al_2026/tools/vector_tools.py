
'''
Tools for vector manipulations

1. cart2polar
2. polar2cart
3. vector_rotation
4. pca_rotation
5. draw_vector (copied from someone!)

u, v = cart2polar(velocidade, direction)

::> converts a pair or array from polar to carteian, in geographical reference

velocity, direction = polar2cart(u, v)

::> converts a pair or array from cartesian to polar, in geographical reference

ur, vr = vector_rotation(u, v, theta)

::> rotates the vector (or array) clockwise by a degree theta (not radians!)

ur, vr, variance_explained, theta = vector_pca(u, v)  :: lists or arrays

::> rotate the arrays u, v to the nearest x axis by a degree theta (PC1), and return the explained variance
    of 1st and 2nd axis

draw_vector([x0, y0], [x1, y1])

::> draw a nice vector given the start and end coordinates. The vector dimensions must be in the axes one,
    otherwise it doesn't work!

Carlos Schettini, 2022/...
use by your own risk!
https://gutoschettini.github.io/Analise_Dados_Python/
'''
import numpy as np

#################################################################
# Convert cartesian to polar
def cart2polar(x, y):

    x = np.atleast_1d(x)
    y = np.array(y)

    velocity = (x**2 + y**2)**.5
    direction = np.arctan(y/x) *180/np.pi

    for i in range(len(x)):
            if x[i] > 0:
                direction[i] = 90 - direction[i]
            else:
                direction[i] = 270 - direction[i]

    return velocity, direction

#################################################################
# Convert polar to cartesian
def polar2cart(velocity, direction):
    velocity = np.array(velocity)
    direction = np.array(direction)

    u = velocity * np.sin(direction*np.pi/180)
    v = velocity * np.cos(direction*np.pi/180)

    return u, v


#################################################################
# Rotate vectors by angle (clockwise)
def vector_rotation(u, v, theta):
    u = np.array(u)
    v = np.array(v)

    theta_rad = -theta*np.pi/180

    ur = u * np.cos(theta_rad) - v * np.sin(theta_rad)
    vr = u * np.sin(theta_rad) + v * np.cos(theta_rad)

    return ur, vr


#################################################################
# Dimensional reduction - PCA

# rotates the data to the nearest X axis
def pca_rotation(u, v):

    u = np.array(u)
    v = np.array(v)

    isnan = np.isnan(u)
    n_nans = isnan[isnan == True]

    if len(n_nans) > 0:
        u = u[isnan == False]
        v = v[isnan == False]
        print('Warning: ', len(n_nans), ' removed for PCA analysis')


    # monta a matriz (2 x n)
    matrix = np.vstack((u, v))

    cov_matrix = np.cov(matrix)
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

    # sorting
    idx = eigenvalues.argsort()
    idx = np.flip(idx)
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]

    variance_explained = np.round(eigenvalues/np.sum(eigenvalues)*100, 1)

    # pick up!
    PC1 = eigenvectors[:,0]
    PC2 = eigenvectors[:,1]

    theta = np.arctan(PC1[1]/PC1[0])*180/np.pi
    ur, vr = vector_rotation(u, v, theta)

    # data rotation using the eigenvectors
    # don't work, don't know why --> the sense of the PC1 don't give me the right direction all the times
#     ur = PC1[0]*u + PC1[1]*v
#     vr = PC2[0]*u + PC2[1]*v

    return ur, vr, variance_explained, theta

#https://jakevdp.github.io/PythonDataScienceHandbook/05.09-principal-component-analysis.html
# o tamanho do vetor tem que caber no axes, senão dá problema!
def draw_vector(v0, v1, ax=None):
    ax = ax or plt.gca()
    arrowprops=dict(arrowstyle='->',
                    linewidth=2,
                    shrinkA=0, shrinkB=0)
    ax.annotate('', v1, v0, arrowprops=arrowprops)
