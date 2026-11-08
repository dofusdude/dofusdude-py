# ClassLooks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**male** | [**ClassAppearance**](ClassAppearance.md) |  | 
**female** | [**ClassAppearance**](ClassAppearance.md) |  | 

## Example

```python
from dofusdude.models.class_looks import ClassLooks

# TODO update the JSON string below
json = "{}"
# create an instance of ClassLooks from a JSON string
class_looks_instance = ClassLooks.from_json(json)
# print the JSON string representation of the object
print(ClassLooks.to_json())

# convert the object into a dict
class_looks_dict = class_looks_instance.to_dict()
# create an instance of ClassLooks from a dict
class_looks_from_dict = ClassLooks.from_dict(class_looks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


