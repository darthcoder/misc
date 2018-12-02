import sys

def conv_to_Celsius(fa):
    celsius = (fa-32)*0.556
    return celsius

print conv_to_Celsius(98)

temp_list = [10, 20, 30, 40]

for temp in temp_list:
    print conv_to_Celsius(temp)


input_string = raw_input("Enter The Temperature here\n")

temp_float = float(input_string)

print "The temperature in Celsius " + str(conv_to_Celsius(temp_float))
