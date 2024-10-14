# SetsListPaged


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**LinksPaged**](LinksPaged.md) |  | [optional] 
**sets** | [**List[SetListEntry]**](SetListEntry.md) |  | [optional] 

## Example

```python
from dofusdude.models.sets_list_paged import SetsListPaged

# TODO update the JSON string below
json = "{}"
# create an instance of SetsListPaged from a JSON string
sets_list_paged_instance = SetsListPaged.from_json(json)
# print the JSON string representation of the object
print(SetsListPaged.to_json())

# convert the object into a dict
sets_list_paged_dict = sets_list_paged_instance.to_dict()
# create an instance of SetsListPaged from a dict
sets_list_paged_from_dict = SetsListPaged.from_dict(sets_list_paged_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


