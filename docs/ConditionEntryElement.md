# ConditionEntryElement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_meta** | **bool** | true if a type is generated from the Api instead of Ankama. In that case, always prefer showing the templated string and omit everything else. The \&quot;name\&quot; field will have an english description of the meta type. An example for such effects are class sets effects. | [optional] 

## Example

```python
from dofusdude.models.condition_entry_element import ConditionEntryElement

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionEntryElement from a JSON string
condition_entry_element_instance = ConditionEntryElement.from_json(json)
# print the JSON string representation of the object
print ConditionEntryElement.to_json()

# convert the object into a dict
condition_entry_element_dict = condition_entry_element_instance.to_dict()
# create an instance of ConditionEntryElement from a dict
condition_entry_element_form_dict = condition_entry_element.from_dict(condition_entry_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


