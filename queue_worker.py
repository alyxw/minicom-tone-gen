import minicom
import os
import mysql.connector
import creds
import time


while True:
    lastlen = 0
    cnx = mysql.connector.connect(
        host=creds.db_host,
        port=creds.db_port,
        user=creds.db_user,
        password=creds.db_pass,
        database=creds.db_database,
    )
    cur = cnx.cursor()
    cur.execute("SELECT `id`,`message` FROM `messages` ORDER BY `id` ASC LIMIT 1")
    row = cur.fetchall()

    if row:
        firstline = row[0][1]
        if firstline == "$$$CLEAR":
            minicom.clear_display("left", 20)
        else:
            print("clearing")
            minicom.clear_display("left", 1)
            print("displaying " + firstline)
            lastlen = len(firstline)
            minicom.displayMessage(firstline)

        cur.execute("DELETE FROM `messages` WHERE `id`=" + str(row[0][0]))
        cnx.commit()
    else:
        time.sleep(1)
    cnx.close()
