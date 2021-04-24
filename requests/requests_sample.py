import requests

url = "http://www.omdbapi.com/?i=tt3896198&apikey=bd51a16a"
search = input("Enter movie name:")

movies = requests.get(url, params={"s": search})
data = movies.json()["Search"]

for x in range(len(data)):
    print(data[x]["Title"])
    print(data[x]["Year"])
    print("--------------------------------")
