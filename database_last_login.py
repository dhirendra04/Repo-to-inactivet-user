
from sqlalchemy import create_engine
import sqlalchemy

# database details

db_user = 'root'
db_password = 'password'
host = "127.0.0.1"
db_name = 'dheeren'
port = 3306

# Change number of days as per your requirement. It will find user have not logged it from last specified date.
days = 34

# add email id which you don't want to deactivate
exclude_email_address = ('dheeren45@gmail.com','nihar@gmail.com')


# ################################################################################ #
#                             ### Script starts here ####

connection_string = "mysql+pymysql://{0}:{1}@{2}/{3}?host={2}?port={4}".format(db_user, db_password, host, db_name, port)

# engine to the  database
engine = create_engine(connection_string)

# connect to db
connection = engine.connect()


# metadata = sqlalchemy.MetaData()
#
#
# cwd_user = sqlalchemy.Table('cwd_user', metadata, autoload=True, autoload_with=engine)
# cwd_user_attributes = sqlalchemy.Table('cwd_user_attributes', metadata, autoload=True, autoload_with=engine)


print "\n+++++++++++++++ SQL Operation Started +++++++++++++++++\n"


# Convert Date into milliseconds
days_in_seconds = days*24*60*60*1000


# find all the user id those have not logged in from last defined dates
query1 = "SELECT cwd_user_attributes.user_id FROM cwd_user_attributes \
WHERE cwd_user_attributes.attribute_value >= {}".format(days_in_seconds)
result1 = connection.execute(query1).fetchall()


user_ids = tuple([x[0] for x in result1])


query2 = "select id, user_name, email_address from cwd_user where id in {0} and email_address not in {1}".format(user_ids, exclude_email_address)
result2 = connection.execute(query2).fetchall()

print "\n======== User details to deactivate ========"
for row in result2:
      print("user id: {}\t user_name: {}\t email_id: {}\t  ".format(row[0], row[1], row[2]))


# my_option = raw_input("press 'y' or 'Y' to deactivate: ")
# print my_option
# if my_option == 'y' or my_option == 'Y':
#       print("Users deactivation started.... wait")
#       query3 = "update cwd_user " \
#                "set active = 3 " \
#                " where id in {0} and cwd_user.email_address not in {1}".format(user_ids, exclude_email_address)
#       connection.execute(query3)
#       print("Users deactivation Done!!!")
#
# else:
#       print("Not deactivated !!\nExited")
