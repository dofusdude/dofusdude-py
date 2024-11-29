# ListSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**items** | **int** | amount | [optional] 
**level** | **int** |  | [optional] 
**effects** | **Dict[str, List[Effect]]** |  | [optional] 
**equipment_ids** | **List[int]** |  | [optional] 
**is_cosmetic** | **bool** |  | [optional] 

## Example

```python
from dofusdude.models.list_set import ListSet

# TODO update the JSON string below
json = "{}"
# create an instance of ListSet from a JSON string
list_set_instance = ListSet.from_json(json)
# print the JSON string representation of the object
print(ListSet.to_json())

# convert the object into a dict
list_set_dict = list_set_instance.to_dict()
# create an instance of ListSet from a dict
list_set_from_dict = ListSet.from_dict(list_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


