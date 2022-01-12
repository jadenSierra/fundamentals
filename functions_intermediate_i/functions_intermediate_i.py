x = [ [5,2,3], [10,8,9] ] 

x[1][0] = 15

print(x)

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

students[0]["last_name"] = "Bryant"

print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory["soccer"][0] = "Andres"

print(sports_directory)


z = [ {'x': 10, 'y': 20} ]

z[0]["y"] = 30

print(z)

print("*" * 80)

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    data = ""
    for i in range(0,len(students)):
        for name_type, name in students[i].items():
            data += str(name_type) + "-" + str(name) + "\n" 
    return data
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
    # first_name - Michael, last_name - Jordan
    # first_name - John, last_name - Rosales
    # first_name - Mark, last_name - Guillen
    # first_name - KB, last_name - Tonel

print(iterateDictionary(students))


print("*" * 80)

def iterateDictionary2(key_name, some_list):
    names = ""
    for x in some_list:
        names += x[key_name] + "\n";
    return names


print(iterateDictionary2('first_name', students))
print(iterateDictionary2('last_name', students)) 

print("*" * 80)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}



def printInfo(some_dict):


    for key,i in some_dict.items():
        print(f"{len(i)} {key.upper()}")
        for val in i:
            print(f"{val}")
    # for key in some_dict:
    #     print(key)

print(printInfo(dojo))
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

