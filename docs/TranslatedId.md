# TranslatedId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | unique | [optional] 
**name** | **str** | localized name | [optional] 

## Example

```python
from dofusdude.models.translated_id import TranslatedId

# TODO update the JSON string below
json = "{}"
# create an instance of TranslatedId from a JSON string
translated_id_instance = TranslatedId.from_json(json)
# print the JSON string representation of the object
print(TranslatedId.to_json())

# convert the object into a dict
translated_id_dict = translated_id_instance.to_dict()
# create an instance of TranslatedId from a dict
translated_id_from_dict = TranslatedId.from_dict(translated_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


