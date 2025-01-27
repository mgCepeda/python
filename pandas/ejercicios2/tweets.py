import pandas as pd

# Recorrer el DataFrame y verificar la longitud de cada tweet
def mostrar_longitud(tweets):
    for index, row in tweets.iterrows():
        tweet_id = row['tweet_id']
        content_length = len(row['content'])
        
        if content_length > 15:
            print(f"El tweet {tweet_id} tiene una longitud de {content_length}. Es un tweet no válido.")
        else:
            print(f"El tweet {tweet_id} tiene una longitud de {content_length}. Es un tweet válido.")

def id_no_validos(tweets):
    # Filtrar los tweets no válidos (longitud del contenido mayor a 15)
    invalidos_tweets = tweets[tweets['content'].str.len() > 15]
    return invalidos_tweets[['tweet_id']].reset_index(drop=True)


# Datos de ejemplo
data = [[1, 'Let us Code'], [2, 'More than fifteen chars are here!']]

# Crear el DataFrame
tweets = pd.DataFrame(data, columns=['tweet_id', 'content']).astype({'tweet_id':'Int64', 'content':'object'})

mostrar_longitud(tweets)
print("---------------------------------------------------")
print(id_no_validos(tweets))

