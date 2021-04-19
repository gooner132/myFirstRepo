import time, sys

sleep_time = 3
print("Script 'test_script.py is starting !!")
print("Sleeping for " + str(sleep_time) + " seconds!", flush=True)

time.sleep(sleep_time)

print("I'm back!!!", flush=True)

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

test_string = sys.argv[1]
print(test_string)

new_str = ""
for x in test_string:
    new_str = new_str + x + "x"

print(new_str)

# EOF #
