# SpellType

Classification of a spell, with localized short and long labels. Not a playable class, spell grade or monster family.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | [optional] 
**short_name** | **str** |  | [optional] 
**long_name** | **str** |  | [optional] 

## Example

```python
from dofusdude.models.spell_type import SpellType

# TODO update the JSON string below
json = "{}"
# create an instance of SpellType from a JSON string
spell_type_instance = SpellType.from_json(json)
# print the JSON string representation of the object
print(SpellType.to_json())

# convert the object into a dict
spell_type_dict = spell_type_instance.to_dict()
# create an instance of SpellType from a dict
spell_type_from_dict = SpellType.from_dict(spell_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


