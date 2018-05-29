import mysql.connector
Con = mysql.connector.connect(
    user="owe4_bi1_2",
    password="blaat1234",
    host="127.0.0.1",
    database="owe4_bi1_2")
        
    
Cur=Con.cursor()

Cur.execute("insert into blast (description,Evalue,query_cover,blast_id) value ('hallo','12,5','3,5 miljoen',35326)")
Con.commit()

Cur.close()
Con.close()
