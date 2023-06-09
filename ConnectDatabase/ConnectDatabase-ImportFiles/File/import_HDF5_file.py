import h5py
filename = 'H-H1_LOSC_4_V1_-815411200-4096.hdf5'
data = h5py.File(filename,'r')
print(type(data))

for key in data.keys():
    print(key)



print(type(data['meta']))


for key in data['meta'].keys():
    print(key)
