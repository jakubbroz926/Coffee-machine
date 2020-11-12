import random

# rozbalování dat

jmena = ["Pavel", "Petr", "Jana", "Ctirad", "Zbyšek"]
*zbytek, poslední = jmena
print( zbytek, poslední )


# * rodílného množství proměnných na pravé a levé straně
# reversed???

def pozdrav():
    print( "ahoj" )


def obal(f):
    f()


obal( pozdrav )

print(3 + random.random() * 7)
