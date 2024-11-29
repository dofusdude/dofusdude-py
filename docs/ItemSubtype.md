# ItemSubtype


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | [optional] 
**name_id** | **str** | unique | [optional] 

## Example

```python
from dofusdude.models.item_subtype import ItemSubtype

# TODO update the JSON string below
json = "{}"
# create an instance of ItemSubtype from a JSON string
item_subtype_instance = ItemSubtype.from_json(json)
# print the JSON string representation of the object
print(ItemSubtype.to_json())

# convert the object into a dict
item_subtype_dict = item_subtype_instance.to_dict()
# create an instance of ItemSubtype from a dict
item_subtype_from_dict = ItemSubtype.from_dict(item_subtype_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


