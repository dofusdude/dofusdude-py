# MappedEntityListEntry

Compact collection summary. A missing detail field here does not mean the resource lacks that data. Request the single-record endpoint or the collection's full fields to obtain details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | 
**name** | **str** |  | 
**image_urls** | [**Images**](Images.md) |  | [optional] 

## Example

```python
from dofusdude.models.mapped_entity_list_entry import MappedEntityListEntry

# TODO update the JSON string below
json = "{}"
# create an instance of MappedEntityListEntry from a JSON string
mapped_entity_list_entry_instance = MappedEntityListEntry.from_json(json)
# print the JSON string representation of the object
print(MappedEntityListEntry.to_json())

# convert the object into a dict
mapped_entity_list_entry_dict = mapped_entity_list_entry_instance.to_dict()
# create an instance of MappedEntityListEntry from a dict
mapped_entity_list_entry_from_dict = MappedEntityListEntry.from_dict(mapped_entity_list_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


