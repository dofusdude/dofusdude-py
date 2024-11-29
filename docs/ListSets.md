# ListSets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PagedLinks**](PagedLinks.md) |  | [optional] 
**sets** | [**List[ListSet]**](ListSet.md) |  | [optional] 

## Example

```python
from dofusdude.models.list_sets import ListSets

# TODO update the JSON string below
json = "{}"
# create an instance of ListSets from a JSON string
list_sets_instance = ListSets.from_json(json)
# print the JSON string representation of the object
print(ListSets.to_json())

# convert the object into a dict
list_sets_dict = list_sets_instance.to_dict()
# create an instance of ListSets from a dict
list_sets_from_dict = ListSets.from_dict(list_sets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


