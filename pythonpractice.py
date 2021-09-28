counties = ["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

    #Using for function to loop through list
for county in counties: 
    print(county) 

    #Using range function to iterate through lists
for i in range(len(counties)):
    print(counties[i])