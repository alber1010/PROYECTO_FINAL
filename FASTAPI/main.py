from fastapi import FastAPI
#http://127.0.0.1:8000 
import pandas as pd
import sklearn 
app = FastAPI()

df2=pd.read_csv("segundafuncion.csv")
df= pd.read_csv("tercerafuncion.csv")


@app.get("/Play_Time_Genre/{genero}")
def PlayTimeGenre(genero: str):
 
    genero= genero.lower()

    # Filtramos el DataFrame por el género especificado
    df_filtrado = df2[df2['genres'].str.lower() == genero]

    # Encontrar el año con la máxima suma de horas jugadas
    año_max_horas = df_filtrado.loc[df_filtrado['playtime_forever'].idxmax()]

    return("El año con más horas jugadas para el genero " + str(genero).capitalize() + " es " + str(año_max_horas['release_year']))  
 



@app.get("/user_for_genre/{genero}")
def UserForGenre(genero: str):
    # Filtra el dataframe df2 por el género solicitado
    df_genre = df2.loc[df2["genres"].str.lower() == genero.lower()]
    
    # Comprueba si hay datos para el género solicitado
    if df_genre.empty:
        # Devuelve un mensaje de error
        return {"error": f"No hay datos para el género {genero}"}
    # Agrupa el dataframe filtrado por el usuario y suma las horas jugadas
    df_user = df_genre.groupby("user_id").sum()["playtime_forever"]
    # Obtiene el usuario con más horas jugadas para el género solicitado
    user = df_user.idxmax()
    # Filtra el dataframe filtrado por el usuario obtenido
    df_user_genre = df_genre.loc[df_genre["user_id"] == user]
    # Agrupa el dataframe filtrado por el año y suma las horas jugadas
    df_user_year = df_user_genre.groupby("release_year").sum()["playtime_forever"]
    # Crea una lista con la acumulación de horas jugadas por año
    hours = [{"Año": year, "Horas": hours} for year, hours in df_user_year.items()]
    # Devuelve el usuario con más horas jugadas para el género solicitado y la lista de la acumulación de horas jugadas por año en formato JSON
    return {f"Usuario con más horas jugadas para el género {genero}": user, "Horas jugadas": hours}

@app.get("/users_recommend/{ano}")
async def users_recommend(ano: int):
    

    df_year = df.loc[df["release_year"] == ano]

    if df_year.empty:
        
        return {"error": f"No hay datos para el año {ano}"}

   
    df_recommend = df_year[(df_year["recommend"] == 1) &
                            (df_year["sentiment_analysis"].isin([1, 2]))]

 
    df_top = df_recommend.groupby("title")["recommend"].count().sort_values(ascending=False).head(3
                                                                                                  )

    
    top_games = df_top.index.tolist()

    return top_games

@app.get("/users_not_recommend/{ano}")
def UsersNotRecommend(ano: int):
   
    df_year = df.loc[df["release_year"] == ano]
   
    if df_year.empty:
       
        return {"error": f"No hay datos para el año {ano}"}
   
    df_not_recommend = df_year[(df_year["recommend"] == 0) & (df_year["sentiment_analysis"] == 0)]
  
    df_game = df_not_recommend.groupby("title").count()["recommend"]
   
    df_top = df_game.sort_values(ascending= False).head(3)
    
    top = [{f"Puesto {i+1}": game} for i, game in enumerate(df_top.index)]
   
    return top


@app.get("/sentiment_analysis/{año}")
def sentiment_analysis(ano: int):
  
    df_year = df.loc[df["release_year"] == ano]

    if df_year.empty:
      
        return {"error": f"No hay datos para el año {ano}"}
  
    df_sentiment = df_year.groupby("sentiment_analysis").count()["recommend"]
   
    sentiment_names = {0: "Negative", 1: "Neutral", 2: "Positive"}
   
    sentiment_count = {sentiment_names[code]: count for code, count in df_sentiment.items()}
   
    return sentiment_count


df4=pd.read_csv('df4final.csv')
df5=pd.read_csv('dfmachine.csv')

df4.index = df4.index.astype(int)
from sklearn.metrics.pairwise import cosine_similarity



# Calcula la similitud del coseno entre todos los pares de elementos
similarity = cosine_similarity(df4.values)

# Imprime la matriz de similitud


similitud= pd.DataFrame(similarity) 



@app.get("/recomendacion_juego/{codigo}")
def recomendacion_juego(codigo: int):
    # Obtener el índice del juego
    indice = df5.loc[df5['código de videojuegos'] == codigo].index[0]

    # Seleccionar los juegos recomendados
    juegos_recomendados_indices = similitud[indice].sort_values(ascending=False).iloc[1:6].index.tolist()

    # Obtener los títulos de videojuegos
    titulos_recomendados = df5.loc[juegos_recomendados_indices, ['title', 'código de videojuegos']]

    return titulos_recomendados.to_dict(orient='records') 