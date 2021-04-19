

f = open("what.txt", "r")
print(f.read())

test_str = f.read()
new_str = ""

for i in test_str:
    new_str = new_str + i + "x"

print("JJ" + new_str + "KK")

# sleep_time = 3
# print("Script 'test_script.py is starting !!")
# print("Sleeping for " + str(sleep_time) + " seconds!", flush=True)
#
# time.sleep(sleep_time)
#
# print("I'm back!!!", flush=True)
#


# EOF #
