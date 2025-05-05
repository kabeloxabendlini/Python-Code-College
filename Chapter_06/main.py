Kabelo_0 = {'Race': 'Black', 'Age': 19}
print(Kabelo_0)
Kabelo_0['x_position'] = 0
Kabelo_0['y_position'] = 25
print(Kabelo_0)

Kabelo_0 = {'Race': 'Black', 'Age': '19'}
name_value = Kabelo_0.get('name_value', 'with a name value assigned.')
print(name_value)