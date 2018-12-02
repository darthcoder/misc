import sys

def conv(celsius):
    fa = (celsius+32)*9/5
    return celsius

print conv(36)

temp_list = [10, 20, 30, 40]

for temp in temp_list:
    print conv(temp)


input_string = raw_input("Enter The Temperature here\n")

temp_float = float(input_string)

print "The temperature in Celsius " + str(conv(temp_float))
