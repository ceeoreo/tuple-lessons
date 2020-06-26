my_tuple = ('Ceora', 'Ford', [8, 12, 24], 2020)

print(my_tuple)

type(my_tuple)

my_tuple.append(['pizza', 'cookies', 'lasagna'])
# Won't work bc tuples are immutable

my_tuple2 = my_tuple + (['pizza', 'cookies', 'lasagna'],)
print(my_tuple2)