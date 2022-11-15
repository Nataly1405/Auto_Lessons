employees_eleks = ['Danny', 'Ester', 'Ben', 'Joy', 'Rachel', 'Ross']
employees_toshiba = ['Chandler', 'Ross', 'Monica', 'Joey', 'Phoebe', 'Rachel']

employees_toshiba.extend(employees_eleks)
employees_eleks.clear()
print(f'List of Toshiba employees: {employees_toshiba}')
