import pickle
with open('pickled_fruit.pkl','rb') as file:
    data = pickle.load(file)
print(data)