# GetGameSearch200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the hit. The query could still have matched with the description only. | [optional] 
**ankama_id** | **int** | Ankama ID for retrieving more details in the type specific endpoint. | [optional] 
**type** | **str** | Type classification | [optional] 

## Example

```python
from dofusdude.models.get_game_search200_response_inner import GetGameSearch200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGameSearch200ResponseInner from a JSON string
get_game_search200_response_inner_instance = GetGameSearch200ResponseInner.from_json(json)
# print the JSON string representation of the object
print GetGameSearch200ResponseInner.to_json()

# convert the object into a dict
get_game_search200_response_inner_dict = get_game_search200_response_inner_instance.to_dict()
# create an instance of GetGameSearch200ResponseInner from a dict
get_game_search200_response_inner_form_dict = get_game_search200_response_inner.from_dict(get_game_search200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


