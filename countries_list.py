
countries = ["Chile","Argentina","Peru","Brazil"]

countries.append("Venezuela")
countries.append("Zimbabwe")
countries.append("Denmark")

countries.sort()

countries.insert(0,"United States")

countries.remove("Argentina")

for con in countries:
    print(con)