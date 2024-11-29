# ListItemGeneral


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | [**TranslatedId**](TranslatedId.md) |  | [optional] 
**item_subtype** | [**ItemSubtype**](ItemSubtype.md) |  | [optional] 
**level** | **int** |  | [optional] 
**image_urls** | [**Images**](Images.md) |  | [optional] 

## Example

```python
from dofusdude.models.list_item_general import ListItemGeneral

# TODO update the JSON string below
json = "{}"
# create an instance of ListItemGeneral from a JSON string
list_item_general_instance = ListItemGeneral.from_json(json)
# print the JSON string representation of the object
print(ListItemGeneral.to_json())

# convert the object into a dict
list_item_general_dict = list_item_general_instance.to_dict()
# create an instance of ListItemGeneral from a dict
list_item_general_from_dict = ListItemGeneral.from_dict(list_item_general_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


