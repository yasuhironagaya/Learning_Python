# Arithmetic operators
a = 10
b = 3

print("Arithmetic operators:")
print("Addition (a + b):", a + b)
print("Subtraction (a - b):", a - b)
print("Multiplication (a * b):", a * b)
print("Division (a / b):", a / b)
print("Modulus (a % b):", a % b)
print("Exponentiation (a ** b):", a ** b)
print("Floor division (a // b):", a // b)

# Comparison operators
print("\nComparison operators:")
print("Equal (a == b):", a == b)
print("Not equal (a != b):", a != b)
print("Greater than (a > b):", a > b)
print("Less than (a < b):", a < b)
print("Greater than or equal to (a >= b):", a >= b)
print("Less than or equal to (a <= b):", a <= b)

# Logical operators
print("\nLogical operators:")
print("and (a > 5 and b < 5):", a > 5 and b < 5)
print("or (a > 5 or b > 5):", a > 5 or b > 5)
print("not (not(a > 5 and b < 5)):", not(a > 5 and b < 5))

# Bitwise operators
print("\nBitwise operators:")
print("AND (a & b):", a & b)
print("OR (a | b):", a | b)
print("XOR (a ^ b):", a ^ b)
print("NOT (~a):", ~a)
print("Shift left (a << 2):", a << 2)
print("Shift right (a >> 2):", a >> 2)

# Assignment operators
print("\nAssignment operators:")
a += b
print("Addition (a += b):", a)
a -= b
print("Subtraction (a -= b):", a)
a *= b
print("Multiplication (a *= b):", a)
a /= b
print("Division (a /= b):", a)
a %= b
print("Modulus (a %= b):", a)
a **= b
print("Exponentiation (a **= b):", a)
a //= b
print("Floor division (a //= b):", a)
a &= b
print("Bitwise AND (a &= b):", a)
a |= b
print("Bitwise OR (a |= b):", a)
a ^= b
print("Bitwise XOR (a ^= b):", a)
a <<= b
print("Shift left (a <<= b):", a)
a >>= b
print("Shift right (a >>= b):", a)

# Identity operators
print("\nIdentity operators:")
print("is (a is b):", a is b)
print("is not (a is not b):", a is not b)

# Membership operators
print("\nMembership operators:")
my_list = [1, 2, 3, 4, 5]
print("in (3 in my_list):", 3 in my_list)
print("not in (6 not in my_list):", 6 not in my_list)
