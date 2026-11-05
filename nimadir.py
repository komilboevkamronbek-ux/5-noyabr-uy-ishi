#              1-masala
# def Test(a:list):
#     max = -1
#     ntj = 0
#     for i in set(a):
#         if a.count(i) > max:
#             max = a.count(i)
#             ntj = i

#     return ntj
# lst = [2, 2, 1, 1, 1, 2, 2]
# print(Test(lst))

#              2-masala
def search_by_genre(cinema:list,genre:str):
    new = []
    for i in cinema:
        if i["genre"] == genre:
            new.append(i)
    return new

cinema = [
    {"title": "Avatar", "genre": "Fantastika", "price": 40000},
    {"title": "Sherlock", "genre": "Detektiv", "price": 30000},
    {"title": "Oq yo'l", "genre": "Drama", "price": 25000},
    {"title": "Dune", "genre": "Fantastika", "price": 35000}
]

print(search_by_genre(cinema, "Fantastika"))
print(search_by_genre(cinema, "Drama"))
print(search_by_genre(cinema, "Komediya"))
print(search_by_genre([], "Boevik"))
print(search_by_genre(cinema, "Detektiv"))





