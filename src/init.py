import psycopg2

def main():
    conn = psycopg2.connect(
        user='postgres',
        password='github-pulls',
        host='github-skills.cubvdlwe6gij.us-east-1.rds.amazonaws.com',
        port='5432',
        database='skills'
    )

    print("Connected... \n\n")
    
    cursor = conn.cursor()
    with open("./src/init.psql", "r") as file:
        query = file.read()
        cursor.execute(query)

    cursor.execute("SELECT * FROM public.\"API_specific\"")
    for row in cursor: print(row)

    conn.close()

main()