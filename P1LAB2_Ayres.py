#CTI 110
#P1LAB2-Recepit
#Ayres
#10/1/24
print('P1LAB2')
#today do a resturant that has only hotdogs and icecream

# declare aour variables
num_hotdogs =0
num_icecream = 0
hotdog_cost=12.99
icecream_cost=5.00

print('Can i take your order?')
# we have to convert their input to an int
num_hotdogs=int(input('How many Hotdogs? '))

print('You Ordered',num_hotdogs,'Hotdogs')

num_icecream=int(input('How many Ice cream Cones do ou want?'))
print('You Ordered', num_icecream,'IceCream Cones')


hotdog_cost=num_hotdogs*hotdog_cost

icecream_cost=num_icecream*icecream_cost

total_cost=num_hotdogs*hotdog_cost+num_icecream*icecream_cost

#Print the recipt
print('_'*30)
print(num_hotdogs,'hotdog\t$',hotdog_cost)
print(num_icecream,'IceCream Cone\t$', icecream_cost)
print('_'*30)
print('Total',total_cost)

