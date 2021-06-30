data.name
'''
0  Luther N. Gonzalez
1    Charles M. Young
2        Terry Lawson
3       Kristen White
4      Thomas Logsdon
'''

#Extracting first names

data.name.str.split(" ").map(lambda x: x[0])
'''
0     Luther
1    Charles
2      Terry
3    Kristen
4     Thomas
'''

#Extracting last names
data.name.str.split(" ").map(lambda x: x[-1])
'''
0    Gonzalez
1       Young
2      Lawson
3       White
4     Logsdon
'''
#String extraction example
data.title.head()
'''
0                      Toy Story (1995)
1                        Jumanji (1995)
2               Grumpier Old Men (1995)
3              Waiting to Exhale (1995)
4    Father of the Bride Part II (1995)
'''

data.title.str.split("(", n=1, expand=True)[1].str.split(")", n=1, expand=True)[0]
'''
0    1995
1    1995
2    1995
3    1995
4    1995
'''
