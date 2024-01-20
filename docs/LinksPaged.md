# LinksPaged


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **str** |  | [optional] 
**prev** | **str** |  | [optional] 
**next** | **str** |  | [optional] 
**last** | **str** |  | [optional] 

## Example

```python
from dofusdude.models.links_paged import LinksPaged

# TODO update the JSON string below
json = "{}"
# create an instance of LinksPaged from a JSON string
links_paged_instance = LinksPaged.from_json(json)
# print the JSON string representation of the object
print LinksPaged.to_json()

# convert the object into a dict
links_paged_dict = links_paged_instance.to_dict()
# create an instance of LinksPaged from a dict
links_paged_form_dict = links_paged.from_dict(links_paged_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


