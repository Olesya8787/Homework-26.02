user = {
    "name" : "John",
    "age" : 23,
    "friends" : [ 
        "Mike", "Bob" , "Joe"
    ],
    "skills" : ("HTML", "CSS", "JS")
}
count = user["friends"].count('Mike')
print(count)
if count >0 :
    newUser = {
       "name" : "Mike"
    }  
    print(newUser)

    user_age = input("Enter your age : ")
    result = 2023 - int(user_age)
    print(result)

del user ["skills"]
print(user)
user["skills"] = ["Python" , "QA"  , "Selenium"]
print(user)

sorted_arr = sorted(user ["friends"] )
print(sorted_arr)

Bob_index = (user["friends"]).index("Bob")
print(Bob_index)

user["friends"].append( "Taras ")
user["friends"].append( "Danya ")
user["friends"].append( "Bidden ")
print(user["friends"])

skills = len(user["skills"])
print(skills)    