def genrateTable(n):
    Table = ""
    for i in range(1,11):
        Table += f"{n} x {i} = {n*i}\n"

    with open(f"table/tables_{n}.txt", "w") as f:
        f.write(Table)



for i in range(2, 21):
    genrateTable(i)
