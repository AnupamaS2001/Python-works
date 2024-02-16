frameworks=[
    {"id":1,"name":"django","rating":5,"language":"python"},
    {"id":2,"name":"angular","rating":4,"language":"typescript"},
    {"id":3,"name":"react","rating":5,"language":"javascript"},
    {"id":4,"name":"spring","rating":3,"language":"java"},
    {"id":5,"name":"asp.net","rating":2,"language":"c#"},
    {"id":6,"name":"flask","rating":3,"language":"python"},
]

# for fw in frameworks:
#     print(fw.get("name"))

# for fw in frameworks:
#     print(fw.get("rating"))

# fws=[fw.get("name") for fw in frameworks]
# print(fws)

# fw_rate=[fw.get("rating") for fw in frameworks]
# print(fw_rate)


# # for fw in frameworks:
# #     if fw.get("language")=="python":
# #         print(fw.get("name"))

# fws=[fw.get("name") for fw in frameworks if(fw["language"]=="python")]
# print(fws)

# python=[i.get("name") for i in frameworks if i.get("rating")==5]
# print(python)

filter=[i.get("name")for i in frameworks if i.get("id") in range(1,4)]
print(filter)


lowest_rating=min(frameworks,key=lambda fw:fw.get("rating"))
print(lowest_rating)


highest_rating=min(frameworks,key=lambda fw:fw.get("rating"))
print(highest_rating)
 
 
srt=sorted(frameworks,reverse=True,key=lambda fw:fw.get("rating"))
print(srt)
