import random

when = ["Few days ago","Few years ago","Few months ago","Few weeks ago","On 15th august","On 20th September","On 10th July"]
who = ["Elizabeth","John","Aniket","Rahul","Sara","Baldev","Rubi","Jim"]
residence = ["India","France","Russia","America","Germany","China","Korea"]
went = ["cricket tournament","volleyball competition","Hackathon","Gym","School","Party","Club","Family function"]
happened = ["made a lot of friends","Eats a lot of chocolates","Drinks a lot of water","found an old cycle","challenged everyone to compete"]

print(random.choice(when),random.choice(who),"lived in",random.choice(residence),"went to a",random.choice(went),"and",random.choice(happened))


# Sample output
# --------------------------------------------------------------------------------
# Few days ago John lived in France went to a Hackathon and made a lot of friends
# --------------------------------------------------------------------------------
