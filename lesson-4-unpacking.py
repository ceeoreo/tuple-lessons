my_tuple = ('Ceora', 'Ford', [8, 12, 24], 2020)

print(my_tuple)

type(my_tuple)

my_tuple2 = my_tuple + (['pizza', 'cookies', 'lasagna'],)
print(my_tuple2)
(name, last_name, favorite_nums, current_yr, foods) = my_tuple2

print(foods)