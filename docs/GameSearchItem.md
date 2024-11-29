# GameSearchItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**GameSearchType**](GameSearchType.md) |  | [optional] 
**level** | **int** |  | [optional] 
**image_urls** | [**Images**](Images.md) |  | [optional] 

## Example

```python
from dofusdude.models.game_search_item import GameSearchItem

# TODO update the JSON string below
json = "{}"
# create an instance of GameSearchItem from a JSON string
game_search_item_instance = GameSearchItem.from_json(json)
# print the JSON string representation of the object
print(GameSearchItem.to_json())

# convert the object into a dict
game_search_item_dict = game_search_item_instance.to_dict()
# create an instance of GameSearchItem from a dict
game_search_item_from_dict = GameSearchItem.from_dict(game_search_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


