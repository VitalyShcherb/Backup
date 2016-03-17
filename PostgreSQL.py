import psycopg2

try:
    conn = psycopg2.connect("dbname='itan_articles' user='itan_user' host='itan.heliohost.org' password='krokodil11'")
except:
    print "I am unable to connect to the database"






