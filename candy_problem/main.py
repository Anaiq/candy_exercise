friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]

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
    print(f"function 1:candie: candie count - {candie_count_dict}")
    return candie_count_dict


#2
def create_new_candy_data_structure(favorites):
    # create a dict of candy keys whose values are list of friends that like that candy
    candy_set = set() #this gets a collection of the UNIQUE candy without duplicates

    for friends in favorites:
        for candy in friends[1]:
            candy_set.add(candy)

    candy_dict = {}

    for candy in candy_set:
        candy_dict[candy] = []

    for friends in favorites:
        friend_name = friends[0]
        candy_list = friends[1]
        for candy in candy_list:
            candy_dict[candy].append(friend_name)

    print(f"function 2: collection of friends who like certain candies- {candy_dict}")
    return candy_dict


#3
def get_friends_who_like_specific_candy(data, candy_name):
    pass

#4
def create_candy_set(data):
    pass 



get_friends_favorite_candy_count(friend_favorites)
create_new_candy_data_structure(friend_favorites)
# get_friends_who_like_specific_candy(friend_favorites, candy_name)
# create_candy_set(friend_favorites)