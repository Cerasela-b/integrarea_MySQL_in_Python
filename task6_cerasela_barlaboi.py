import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = 'RorysiTigrutz',
    database = 'movies'
)

if(conn == None):
    print("There is no connection to database.")
else:
    print('Connection is created.')
    
cursor = conn.cursor

print("Connection established successfully, and the cursor has been created.")

query =  """
SELECT g.name_genre AS genre, m.budget
FROM movie m
JOIN genremovie gm ON m.id_movie = gm.movie_id
JOIN genre g ON gm.genre_id = g.genre_id;
"""
df_movies = pd.read_sql(query, conn)

conn.close()

print(df_movies)

average_budgets = df_movies.groupby("genre")["budget"].mean()

print("Bugetul mediu pe gen este: ")
print(average_budgets)

print("\n Statistici descriptive ale întregului DataFrame: ")
print(df_movies.describe())

plt.figure(figsize=(12, 6))
plt.bar(average_budgets.index, average_budgets.values, color='purple')
plt.title("Bugetul Mediu al Filmelor pe Gen", fontsize=16)
plt.xlabel("Genul Filmului", fontsize=12)
plt.ylabel("Buget Mediu ($)", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()