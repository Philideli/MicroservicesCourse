import sqlite3

path = "./services/db2_service/"

conn = sqlite3.connect(f'{path}flowers.db')

sql = "SELECT * FROM flower"
cur = conn.execute(sql).fetchall()

queries = f"INSERT INTO flower VALUES\n"
for flower in cur:
    queries += "("
    for i in range(len(flower)):
        if i == 0: continue
        if type(flower[i]) == int:
            queries += f"{flower[i]},"
        elif type(flower[i]) == str:
            queries += f"'{flower[i]}',"
        # possible space for photos?..
        if i == len(flower)-1:
            queries = queries[:-1]
    queries += ")\n"
# print(queries)

with open(f"{path}/migrations/tmp.txt", "w") as file:
    file.write(queries)