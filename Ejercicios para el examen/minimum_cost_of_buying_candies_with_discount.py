# A shop is selling candies at a discount. For every two candies sold, the shop gives a third candy for free.

# The customer can choose any candy to take away for free as long as the cost of the chosen candy is less than or equal to the minimum cost of the two candies bought.

# For example, if there are 4 candies with costs 1, 2, 3, and 4, and the customer buys candies with costs 2 and 3, they can take the candy with cost 1 for free, but not the candy with cost 4.
# Given a 0-indexed integer array cost, where cost[i] denotes the cost of the ith candy, return the minimum cost of buying all the candies.

 

# Example 1:

# Input: cost = [1,2,3]
# Output: 5
# Explanation: We buy the candies with costs 2 and 3, and take the candy with cost 1 for free.
# The total cost of buying all candies is 2 + 3 = 5. This is the only way we can buy the candies.
# Note that we cannot buy candies with costs 1 and 3, and then take the candy with cost 2 for free.
# The cost of the free candy has to be less than or equal to the minimum cost of the purchased candies.
# Example 2:

# Input: cost = [6,5,7,9,2,2]
# Output: 23
# Explanation: The way in which we can get the minimum cost is described below:
# - Buy candies with costs 9 and 7
# - Take the candy with cost 6 for free
# - We buy candies with costs 5 and 2
# - Take the last remaining candy with cost 2 for free
# Hence, the minimum cost to buy all candies is 9 + 7 + 5 + 2 = 23.
# Example 3:

# Input: cost = [5,5]
# Output: 10
# Explanation: Since there are only 2 candies, we buy both of them. There is not a third candy we can take for free.
# Hence, the minimum cost to buy all candies is 5 + 5 = 10.

# Recibo el array
# crear variable para la sumatoria
# valido si el array tiene una longitud de 2 sumo y retorno
# creo un nuevo array copiando el original y lo ordeno de mayor a menor
# Hago el loop
# hacer los grupos de 3 
# sumar los 2 primero y no el 3 sumando a la variable
# si no se completa el grupo se suma todo
# retornar

def minimum_cost(cost):
    sum_min = 0
    n = len(cost)
    if n < 3:
        return sum(cost)
    
    new_cost = cost[:]
    new_cost.sort(reverse=True)
    for i in range(n):
        if i % 3 == 0:
            sum_min += new_cost[i]
        if i % 3 == 1:
            sum_min += new_cost[i]
        #el 3 es gratis no hay que sumar 
        #if i % 3 == 2:
            #continue

    #Otra forma de hacer lo solo recorriendo indices 
    #aqui esta la clave le decimos comienza en el indice 0, al len del array, de 3 en 3
    #entonces si el array tiene 9 primeo itera del 0 al 2, 3 veces
    #for i in range(0, n, 3): 
            
        #total += new_cost[i]              # primero del grupo
        #if i + 1 < n:
            #total += new_cost[i + 1]      # segundo del grupo
        # i + 2 es el gratis (si existe, no se suma)
            #total += new_cost[i + 2]      # no se suma solo es representativo para entender
    return sum_min

cost = [1,2,3]
#cost = [6,5,7,9,2,2]
#cost = [5,5]
print(minimum_cost(cost))