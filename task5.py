non_unique_names = ['Ron Weasley', 'Garry potter', 'Hermione Granger', 'Severus Snape',
                    'Hagrid Rubeus', 'Severus Snape', 'Bill Weasley', 'Garry potter'
                    ]

non_duplicate_names = list(dict.fromkeys(non_unique_names))
print(f'Unique names from the list: {non_duplicate_names}')
