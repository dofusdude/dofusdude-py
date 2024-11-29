# PagedLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **str** |  | [optional] 
**prev** | **str** |  | [optional] 
**next** | **str** |  | [optional] 
**last** | **str** |  | [optional] 

## Example

```python
from dofusdude.models.paged_links import PagedLinks

# TODO update the JSON string below
json = "{}"
# create an instance of PagedLinks from a JSON string
paged_links_instance = PagedLinks.from_json(json)
# print the JSON string representation of the object
print(PagedLinks.to_json())

# convert the object into a dict
paged_links_dict = paged_links_instance.to_dict()
# create an instance of PagedLinks from a dict
paged_links_from_dict = PagedLinks.from_dict(paged_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


