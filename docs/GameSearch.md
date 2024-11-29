# GameSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | [**GameSearchType**](GameSearchType.md) |  | [optional] 
**item_fields** | [**GameSearchItem**](GameSearchItem.md) |  | [optional] 

## Example

```python
from dofusdude.models.game_search import GameSearch

# TODO update the JSON string below
json = "{}"
# create an instance of GameSearch from a JSON string
game_search_instance = GameSearch.from_json(json)
# print the JSON string representation of the object
print(GameSearch.to_json())

# convert the object into a dict
game_search_dict = game_search_instance.to_dict()
# create an instance of GameSearch from a dict
game_search_from_dict = GameSearch.from_dict(game_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


