#========================================== Update Values in Dictionaries and Lists ========================================
def updateval(arr):
    
    value = []

    for i in range(0,len(arr),1):
        value = arr[1]

    for i in range(0,len(value),1):
        value[0] = 15


    return [arr[0],value]


def lastname(arr):

    student = []

    for i in range(0,len(arr),1):
        student = arr[0]
    
    student['last_name'] = 'Bryant'

    return [student,arr[1]]


def sportsname():

    soccerplayers = sports_directory['soccer']

    for i in range(0,len(soccerplayers),1):
        soccerplayers[0] = 'Andres'
    
    return soccerplayers

def changeval (arr):

    ychanged = []

    for i in range(0,len(arr),1):
        ychanged = arr[0]
    ychanged['y'] = 30

    return[ychanged]



#============================================== Information Provided ======================================================

x = [ [5,2,3], [10,8,9] ] 

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#==========================================================================================================================
x = updateval(x)
print (x)

students = lastname(students)
print (students)

sports_directory['soccer'] = sportsname()
print(sports_directory)

z = changeval(z)
print(z)


#========================================== Iterate Through a List of Dictionaries ========================================
def iterateDictionary(some_list):
    for i in range(0,len(some_list),1):
        print("first_name - " + some_list[i]['first_name'] + "," + " last name - " + some_list[i]['last_name'])
#============================================== Information Provided ======================================================

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
#==========================================================================================================================

iterateDictionary(students)

#========================================== Get Values From a List of Dictionaries ========================================

def iterateDictionary2(key_name, some_list):
    
    listdata = []

    listdata = some_list[key_name]

    for i in range (0, len(listdata),1):
        print(listdata[i])

students2 = {
                'first_name': ['Michael','John','Mark','KB'],
                'last_name': ['Jordan', 'Rosales', 'Guillen', 'Tonel']
                }

iterateDictionary2('first_name',students2)
iterateDictionary2('last_name',students2)



#========================================== Iterate Through a Dictionary with List Values ========================================



def print_info(some_dict):
    for key,val in some_dict.items():
        print("--------------")
        print(f"{len(val)} {key.upper()}")
        for i in range(0, len(val)):
            print(val[i])





dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

print_info(dojo)