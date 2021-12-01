def yarn(name,noun,place,adv,adj1,adj2,verb,food1,food2):

    print(f"{name} is planning a trip to {place}.")  
    print(f"{name} is looking forward to trying the local cuisine, including {adj1} {food1} and {food2}.")
    print(f"{name} will have to learn the local language {adv} to make it easier to {verb} with people.")
    print(f"{name} has a bucket list of sights to see, including the {noun} museum and the {adj2} mountains.")
#---------------------------------------------------------------------------------------------------------------
print("""
   |\---/|
   | ,_, |          Welcome to
    \_`_/-..----.
 ___/ `   ' ,""+ \  Spin the Yarn  by:- utkarsh575
(__...'   __\    |`.___.';
  (_,...'(_,.`__)/'.....+
""")
print("Let`s play Spin the Yarn! >_< ")

name = input("Enter a name: ")
adj1 = input("Enter an adjective: ")
adj2 = input("Enter an adjective: ")
adv = input("Enter an adverb: ")
food1 = input("Enter a food: ")
food2 = input("Enter another food: ")
noun = input("Enter a noun: ")
place = input("Enter a place: ")
verb = input("Enter a verb: ")
print("Mad Sentences incoming XD... ")

yarn(name,noun,place,adv,adj1,adj2,verb,food1,food2)



