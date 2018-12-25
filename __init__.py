
class addonepoint:
	def __init__(self):
		self.res = []
		self.path = False
	def checkm4add1pt(self, m4gbnumber, m5gbnumber, m1_number, m2_number):
		m4gbnumber = str(m4gbnumber)
		m5gbnumber = str(m5gbnumber)
		with open('p2n4.txt') as f: content = f.readlines()
		#print(content[:100])
		newcontent = []
		for i in range(len(content)): newcontent.append(content[i].split(';')[:2]) 
		total = []
		for i in range(len(newcontent)):
			string2 = ''
			string3 = []

			if newcontent[i][0] == m4gbnumber:
				string2 = newcontent[i][1]
				string3 = string2.split('},')
				list1 = []
				if len(string3) == m1_number:
					for i in range(len(string3)):
						newlist = []
						for j in range(len(string3[0])):
							if string3[i][j] in ['0','1']:
								newlist.append(int(string3[i][j]))
						list1.append(newlist)
						
					total.append(list1)
		m4gb6 = total
		newcontent = []
		for i in range(len(content)): newcontent.append(content[i].split(';')[:2]) 
		total = []
		for i in range(len(newcontent)):
			string2 = ''
			string3 = []

			if newcontent[i][0] == m5gbnumber:
				string2 = newcontent[i][1]
				string3 = string2.split('},')
				list1 = []
				if len(string3) == m2_number:
					for i in range(len(string3)):
						newlist = []
						for j in range(len(string3[0])):
							if string3[i][j] in ['0','1']:
								newlist.append(int(string3[i][j]))
						list1.append(newlist)
						
					total.append(list1)
		m5gb1 = total
		for set1 in m4gb6:
			for set2 in m5gb1:
				flag = 0
				for set11 in set1:
					if set11 in set2:
						flag += 1
				if flag == m1_number:
					self.path = True
					#print( str(m4gbnumber) + ' Gbs for ' + str(m1_number) +' points to ' + str(m5gbnumber) + ' Gbs for ' + str(m2_number) +' points')
					#print( str(m1_number ) + ' points',set1, 'to ' + str(m2_number)+ ' points ', set2)
					self.res.append((set1, set2))
		print('end of the test')
	
	def checkaddone(self, m4gbnumber, m5gbnumber, m1_number, m2_number):
		self.checkm4add1pt(m4gbnumber, m5gbnumber, m1_number, m2_number)
		
		if not self.path :
			print(self.path)
			print('There is no add one point path for '+ str(m4gbnumber) +' Gbs ' + str(m1_number) + ' points to ' +  str(m5gbnumber) +' Gbs ' + str(m2_number) + ' points' )
		else:# write result to file:
			print(self.path)
			print( str(m4gbnumber) + ' Gbs for ' + str(m1_number) +' points to ' + str(m5gbnumber) + ' Gbs for ' + str(m2_number) +' points')
			#print( str(m1_number ) + ' points',set1, 'to ' + str(m2_number)+ ' points ', set2)
			file = open(str(m4gbnumber)+'gb'+str(m1_number)+'pts'+str(m5gbnumber)+'gb'+str(m2_number)+'pts'+'.txt','w') 
			file.write(str(self.res))
			print('file has been created in your folder')


