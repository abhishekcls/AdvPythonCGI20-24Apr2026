import logging

logging.basicConfig(level=logging.INFO)#if you don't mention then by default it ignores info and debug
#logging.basicConfig(level=10)
try:
    age=input("Enter Age: ")
    age=int(age)
    #print(ab)
    print(age,type(age))
    print(age+10)
    #raise ValueError
except NameError as ne:
    logging.error(f"Variable {ne.name} not defined")
except ValueError:
    logging.critical("Enter numbers only")
except Exception:
    logging.error("Handles all errors")
else:
    logging.info("Success")
finally:
    logging.warning("Success or Error")

print("Done")

'''
info 10
debug 20
warning 30
error 40
critical 50
'''

'''
try
except
else
finally
raise
'''