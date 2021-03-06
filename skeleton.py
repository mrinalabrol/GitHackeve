#Welcome to HackEve v20

#takes a string s as argument and converts it from binary to decimal form
def bin_to_dec(s):
	a = s[::-1]
	dec = 0
	for ind, i in enumerate(a):
		dig =  int(i)
		mul = dig*2**ind
		dec = dec + mul
	str1 = str(dec)
	return str1

	#return n #Number n in decimal form will be returned


#takes a number n as argument and converts it from decimal to hexadecimal form
def dec_to_hex(n):
	lis = []
	digits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
	dec = int(n)
	while(dec != 0):
		rem = dec % 16
		lis.append(digits[rem])
		dec = dec // 16
	lis.reverse()
	str1 = ''.join(lis)

	return str1 #String str1 will be returned in hexadecimal form

#takes a string s as argument in hexadecimal form and returns its 1's compliment
def hex_compliment(s):
	s=str(input())
	x=list(s)
	for i in range(0, len(x)):
		if x[i]=='0':
			x[i]='1'
		elif x[i]=='1':
			x[i]='0'
	t=''.join(x)
	return t #String str1 will be returned as 1's compliment



s = input("Enter the binary string: ")

digits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
a = bin_to_dec(s)
b = dec_to_hex(a)
c = hex_compliment(b)


print("Final output is",c)