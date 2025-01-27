import pandas as pd

# Datos de ejemplo
data_customers = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
customers = pd.DataFrame(data_customers, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})

data_orders = [[1, 3], [2, 1]]
orders = pd.DataFrame(data_orders, columns=['id', 'customerId']).astype({'id':'Int64', 'customerId':'Int64'})

# Función para encontrar clientes que no han hecho ninguna compra
def clientes_sin_compras(customers, orders):
    # Identificar los clientes que no están en la columna customerId de orders
    clientes_con_compras = orders['customerId'].unique()

    # Filtrar los clientes que no han comprado
    clientes_sin_compras = customers[~customers['id'].isin(clientes_con_compras)]
    
    return clientes_sin_compras

# Resultado
print(clientes_sin_compras(customers, orders))
