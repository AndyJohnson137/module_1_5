immutable_var = (1, 2, 'a', 'b')
rem_sps = str(immutable_var).replace(' ', "")
print("Immutable tuple: " + str(rem_sps))
# immutable_var[1] = 6
# print(immutable_var) Кортеж не поддерживает обращение по элементам и соответственно не может их изменить.
mutable_list = [1, 2, 'a', 'b', 'Modified']
mutable_list[1] = 6
rem_sps1 = str(mutable_list).replace(' ', "")
print("Mutable list: " + rem_sps1)
