import scipy.io

filename = 'workspace.mat'
mat = scipy.io.loadmat(filename)
print(type(mat))

