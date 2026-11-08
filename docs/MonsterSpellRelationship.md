# MonsterSpellRelationship


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | 
**name** | **str** |  | 
**grade** | **int** | The spell grade assigned to this monster grade. | 
**url** | **str** | URL for the assigned spell grade. Includes the &#x60;grade&#x60; query parameter. | 
**image_urls** | [**Images**](Images.md) |  | [optional] 

## Example

```python
from dofusdude.models.monster_spell_relationship import MonsterSpellRelationship

# TODO update the JSON string below
json = "{}"
# create an instance of MonsterSpellRelationship from a JSON string
monster_spell_relationship_instance = MonsterSpellRelationship.from_json(json)
# print the JSON string representation of the object
print(MonsterSpellRelationship.to_json())

# convert the object into a dict
monster_spell_relationship_dict = monster_spell_relationship_instance.to_dict()
# create an instance of MonsterSpellRelationship from a dict
monster_spell_relationship_from_dict = MonsterSpellRelationship.from_dict(monster_spell_relationship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


