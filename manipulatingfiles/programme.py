user_name = raw_input("enter username")
file = open("names.txt","r+")
if user_name  not in file.readline():
    file.write(user_name)
    file.close()
    print "success" + user_name + "entered in file"
else:
    print "error" +user_name + "in database"
    file.close()
