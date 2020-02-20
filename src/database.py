import psycopg2

def query_db():
    db1 = []
    db2 = []
    db3 = []
    db4 = []

    conn = psycopg2.connect(
        user='postgres',
        password='github-pulls',
        host='github-skills.cubvdlwe6gij.us-east-1.rds.amazonaws.com',
        port='5432',
        database='skills'
    )
    
    cursor = conn.cursor()
    
    with open("./src/init.psql", "r") as file:
        query = file.read()
        cursor.execute(query)

    cursor.execute("SELECT * FROM public.\"API\"") # (api_name, class, count)
    for row in cursor: db1.append(row)
    cursor.execute('SELECT * FROM public."file_API"') # (file_name, api_name, count)
    for row in cursor: db2.append(row)
    cursor.execute('SELECT * FROM public."API_specific"') # (general, specific, api_name_fk)
    for row in cursor: db3.append(row)
    cursor.execute('SELECT * FROM public.file') # (file_name, full_name, project)
    for row in cursor: db4.append(row)
    
    conn.close()
    
    return (db1, db2, db3, db4)