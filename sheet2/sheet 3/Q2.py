fl_number = 1234.5678
bef_int_number = 2
aft_int_number = 3
number = str(fl_number)
integer_part, decimal_part = number.split('.')
a = integer_part[-bef_int_number:]
b = decimal_part[:aft_int_number]
c = float(f"{a}.{b}")

print(c)