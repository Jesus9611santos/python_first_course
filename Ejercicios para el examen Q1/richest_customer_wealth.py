# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

 

# Example 1:

# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6
# Explanation:
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6
# Both customers are considered the richest with a wealth of 6 each, so return 6.
# Example 2:

# Input: accounts = [[1,5],[7,3],[3,5]]
# Output: 10
# Explanation: 
# 1st customer has wealth = 6
# 2nd customer has wealth = 10 
# 3rd customer has wealth = 8
# The 2nd customer is the richest with a wealth of 10.
# Example 3:

# Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
# Output: 17

# primero recibo las accounts
# sumo la account del primer cliente con sum(numeros)
# Guardo el resultado en una variable
# recorro el array de customer con un range para ya no volver hacer el sum del primer account 
# en cada uno hago un sum y lo comparo con mi variable si es mayor lo remplazo
# al final lo retorno

def maximum_wealth(accounts):
        max_num = sum(accounts[0])
        for i in range(1, len(accounts)):
                suma = sum(accounts[i])
                if suma > max_num:
                        max_num = suma
        return max_num

accounts = [[1,2,3],[3,2,1]]
accounts = [[1,5],[7,3],[3,5]]
accounts = [[2,8,7],[7,1,3],[1,9,5]]
print(maximum_wealth(accounts))