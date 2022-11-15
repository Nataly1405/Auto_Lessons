casino_blacklist = {'Chandler Bing', 'Joey Tribbiani', 'Rachel Green',
                    'Monica Geller', 'Phoebe Buffay', 'Ross Geller'
                    }
poker_blacklist = {'Ben Den', 'Luise Zuise', 'Jackie Chan',
                   'Joey Tribbiani', 'Monica Geller', 'Ben Affleck'
                   }
alcohol_blacklist = {'Joey Tribbiani', 'Ron Weasley', 'Garry potter',
                     'Monica Geller', 'Ben Den'}

all_blacklists = casino_blacklist.intersection(poker_blacklist)
all_blacklists = alcohol_blacklist.intersection(all_blacklists)

print(f'Guests from all blacklists:  {all_blacklists}')
