import pytest
from candy_problem.main import * 

def test_get_friends_favorite_candy_count():
    # Arrange
    friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
    ]

    # Act
    result = get_friends_favorite_candy_count(friend_favorites)
    
    # Assert
    assert len(result) == 8
    assert result["lollipop"] == 2
    assert result["laffy taffy"] == 3
    assert result["bubble gum"] == 1
    assert result["milky way"] == 2
    assert result["licorice"] == 1
    assert result["chocolate bar"] == 1
    assert result["nerds"] == 1
    assert result["sour patch kids"] == 1


def test_create_candy_data_structure_type():
    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop”, “bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    # Assert
    assert type(new_candy_data) == dict
    

def test_create_candy_data_structure_values():

    # Arrange
    friend_favorites = [
        ["Sally", ["lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    # Assert
    assert new_candy_data["lollipop"] == ["Sally", "Bob"]
    assert new_candy_data["bubble gum"] == ["Sally"]
    assert new_candy_data["laffy taffy"] == ["Sally", "Arlene", "Carlie"]
    assert new_candy_data["milky way"] == ["Bob", "Arlene"]
    assert new_candy_data["licorice"] == ["Bob"]
    assert new_candy_data["chocolate bar"] == ["Arlene"]
    assert new_candy_data["nerds"] == ["Carlie"]
    assert new_candy_data["sour patch kids"] == ["Carlie"]

    
def test_get_friends_who_like_specific_candy_data_structure():
    #Arrange
    friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
    ]

    # Act
    friends_tuple = get_friends_who_like_specific_candy(friend_favorites, "laffy taffy")

    # Assert
    assert type(friends_tuple) == tuple


def test_get_friends_who_like_specific_candy_values():
    #Arrange
    friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
    ]

    # Act
    friends_tuple = get_friends_who_like_specific_candy(friend_favorites, "laffy taffy")

    # Assert
    assert tuple(["Sally", "Arlene", "Carlie"]) == friends_tuple

def test_create_candy_set_data_structure():
    #Arrange
    friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
    ]

    # Act
    candy_set = create_candy_set(friend_favorites)

    # Assert
    assert type(candy_set) == set


def test_create_candy_set_values():
    #Arrange
    friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
    ]

    # Act
    candy_set = create_candy_set(friend_favorites)

    # Assert
    assert (len(candy_set) == 8)
    assert set([
        "lollipop",
        "bubble gum",
        "laffy taffy",
        "milky way",
        "licorice",
        "nerds",
        "sour patch kids",
        "chocolate bar"
        ]) == candy_set


