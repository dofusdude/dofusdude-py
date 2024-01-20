# CosmeticType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from dofusdude.models.cosmetic_type import CosmeticType

# TODO update the JSON string below
json = "{}"
# create an instance of CosmeticType from a JSON string
cosmetic_type_instance = CosmeticType.from_json(json)
# print the JSON string representation of the object
print CosmeticType.to_json()

# convert the object into a dict
cosmetic_type_dict = cosmetic_type_instance.to_dict()
# create an instance of CosmeticType from a dict
cosmetic_type_form_dict = cosmetic_type.from_dict(cosmetic_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


