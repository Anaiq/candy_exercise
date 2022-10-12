import pytest
from candy_problem.main import * 

# @pytest.mark.skip
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


# @pytest.mark.skip
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
    

@pytest.mark.skip
def test_create_candy_data_structure_values():

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
    