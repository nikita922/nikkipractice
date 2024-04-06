# To use bitwise operators
a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101

c = a & b;        # 12 = 0000 1100
print ("& operator - Value of c is ", c)

c = a | b;        # 61 = 0011 1101
print ("| operator - Value of c is ", c)

c = a ^ b;        # 49 = 0011 0001
print ("^ operator - Value of c is ", c)

c = ~a;           # -61 = 1100 0011
print ("~ operator - Value of c is ", c)

c = a << 2;       # 240 = 1111 0000
print ("<<Left shift operator- Value of c is ", c)

c = a >> 2;       # 15 = 0000 1111
print (">>Right shift operator - Value of c is ", c)