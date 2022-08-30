omnivores_group = {'Ron Weasley', 'Garry potter', 'Hermione Granger'}
vegetarians_group = {'Hagrid Rubeus', 'Albus Dumbledore', 'Severus Snape'}

can_eat_vegetarians = omnivores_group.union(vegetarians_group)
print(f'List of guests who can eat vegetarian food: {can_eat_vegetarians}')
