'''
GCD -> Greatest Common Intiger
'''

def gcd(m,n):
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

gcd(5,10)
