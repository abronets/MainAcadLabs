countries = {'Ukraine':'UA','Italy' : 'IT','Yapan':'YP', 'Australia':'AU', 'USA':'US','Bulgaria':'BG'}
capitals = {'UA':'Kiev', 'IT' : 'Rome', 'YP':'Tokyo', 'AU':'Canberra', 'US':'Washington','BG':'Sofia'}

countries['Poland'] ='PL'
capitals['PL'] = 'Varshava'

for i in countries:
    print('Domain for {} is {}'.format(i,countries[i]))

for i in capitals:
    print('The capital of {} is {}'.format(i,capitals[i]))

for cntryname, iec in countries.items():
    print('Domain for {} is {}.The capital is {}'.format(cntryname, iec, capitals[iec]))

for cntryname, iec in countries.items():
	countries[cntryname] = list(iec, 'COM', 'GOV')




