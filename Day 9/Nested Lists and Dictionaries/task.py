# capitals = {
#     "France" : "Paris",
#     "India" : "Delhi",
# }
#
# travel_log = {
#     "France" : ["Delhi", "Mumbai", "Kolkata"],
#     "Germany":["Stuttgart","Berlin"]
# }
# print(travel_log["France"][1])
#
# nested_list = ["A","B",["C","D"]]
# print(nested_list[2][1])

travel_log = {
    "France" : {
        "cities_visited":["Paris","Little","Dijon"],
        "total_visited": 12
    },
    "Germany":{
        "cities_visited": ["Berlin","Hamburg", "stuttgart"],
        "total_visited" :3
    },
}
print(travel_log["Germany"]["cities_visited"][2])
