import mysql.connector

con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

cursor = con.cursor()


def app(word):
    word1 = word.lower()
    sql = "SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word1
    query = cursor.execute(sql)

    result = cursor.fetchall()
    if result:
        return result
  """   elif:
        sql = "SELECT Definition FROM Dictionary WHERE Expression = '%s%'" % word1
        query = cursor.execute(sql)
        result = cursor.fetchall()
        return result
    else:
        return "No existe esa palabra" """


input_u = input("palabra: ")
resultado = app(input_u)

for row in resultado:
    print(row)
