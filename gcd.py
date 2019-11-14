'''
GCD -> Greatest Common Intiger
'''

# first way to create gcd program 

def gcd1(m,n):
	if m == 0 or n == 0 :
		print 'values must be greater than 0'
	else:	

		small_no = m if m<n else n
		large_no = n if m<n else m
		fn =[]
		i= 1
		while i<small_no+1:
			if small_no%i == 0:
				fn.append(i)
			i = i+1
		i =1
		gn= []
		while i<large_no+1 :
			if large_no%i == 0:
				gn.append(i)
			i = i+1
		
		cn = []
		for f in fn:
			for g in gn:
				if f==g:
					cn.append(f)
		print "GCD of", m," and ",n ,"is", cn[-1]



# 2 . way to create gcd program using recursive while loop.

def gcd2(n,m):
	i=1
	cn = []
	while i<min(n,m)+1:
		if m%i == 0 & n%i == 0:
			cn.append(i)
		i= i+1
	print "GCD of", m," and ",n ,"is", cn[-1]


n = int(input( 'Enter the First no : '))
m = int(input( 'Enter the second no : '))
gcd2(n,m)


