friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]

candy_name = "lollipop"

#1
def get_friends_favorite_candy_count(favorites):
    candie_count_dict = {}

    for friends in favorites:
        for candy in friends[1]:
            if candy not in candie_count_dict:
                candie_count_dict[candy] = 1
            else:
                candie_count_dict[candy] +=1

    # return a dictionary of candy names and the amount of times each candy appears in the `friend_favorites` list.
    print(f"function 1: candie: candie count - {candie_count_dict}\n")
    return candie_count_dict


#2
def create_new_candy_data_structure(favorites):
    # create a dict of candy keys whose values are list of friends that like that candy
    candy_set = set() #this gets a collection of the UNIQUE candy without duplicates

    for friends in favorites:
        for candy in friends[1]:
            candy_set.add(candy)
    print(f"candy set- {candy_set}\n")

    candy_dict = {}

    for candy in candy_set:
        candy_dict[candy] = []

    for friends in favorites:#change name
        friend_name = friends[0]
        candy_list = friends[1]
        for candy in candy_list:
            candy_dict[candy].append(friend_name)
    print(f"function 2: collection of friends who like certain candies- {candy_dict}\n")

    return candy_dict


#3
def get_friends_who_like_specific_candy(favorites, candy_name):
    friends_list = []

    for friend_list in favorites:
        friend_name = friend_list[0]
        candy_list = friend_list[1]
        if candy_name in candy_list:
            friends_list.append(friend_name)

    friends_tuple = tuple(friends_list)
    print(f"function 3: tuple of friends who like specific candy-{friends_tuple}")

    return friends_tuple


#4
def create_candy_set(favorites):
    candy_set = set() #this gets a collection of the UNIQUE candy without duplicates
    

    for friends in favorites:
        for candy in friends[1]:
            candy_set.add(candy)

    print(f"candy set- {candy_set}\n")
    return candy_set
    

get_friends_favorite_candy_count(friend_favorites)
create_new_candy_data_structure(friend_favorites)
get_friends_who_like_specific_candy(friend_favorites, candy_name)
create_candy_set(friend_favorites)