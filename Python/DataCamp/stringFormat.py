
custom_string = 'String formatting'
print(f"{custom_string} is a powerful technique")

######################################

print("Machine learning provides {} the ability to learn {}".format("systems","automatically"))

#########################################

my_string = "{} rely on {} datasets"
method = "Supervised algorithms"
condition = "labeled"

print(my_string.format(method,condition))

########################################
def my_function(a,b):
    return a + b

print(f'If you sum up 10 and 20 the result is {my_function(10,20)}')


############################################
my_number = 4
my_multipler = 7
print(f'{my_number} multipled by {my_multipler} is {my_number * my_multipler}')