import time, sys

print ()

f = open("what.txt", "a")
f.write(sys.argv[1] + "\n")
f.close()


# sleep_time = 3
# print("Script 'test_script.py is starting !!")
# print("Sleeping for " + str(sleep_time) + " seconds!", flush=True)
#
# time.sleep(sleep_time)
#
# print("I'm back!!!", flush=True)
#
print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

# EOF #

