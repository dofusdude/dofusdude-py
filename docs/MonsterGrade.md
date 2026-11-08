# MonsterGrade


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grade** | **int** |  | 
**level** | **int** |  | 
**life_points** | **int** |  | [optional] 
**action_points** | **int** |  | [optional] 
**movement_points** | **int** |  | [optional] 
**grade_xp** | **int** |  | [optional] 
**neutral_resistance** | **int** |  | [optional] 
**earth_resistance** | **int** |  | [optional] 
**fire_resistance** | **int** |  | [optional] 
**water_resistance** | **int** |  | [optional] 
**air_resistance** | **int** |  | [optional] 
**pa_dodge** | **int** |  | [optional] 
**pm_dodge** | **int** |  | [optional] 
**damage_bonus** | **int** |  | [optional] 
**percent_damage_bonus** | **int** |  | [optional] 
**critical_hit_bonus** | **int** |  | [optional] 
**initiative_bonus** | **int** |  | [optional] 
**tackle_bonus** | **int** |  | [optional] 
**tackle_evade** | **int** |  | [optional] 
**max_summon** | **int** |  | [optional] 
**bonus_characteristics** | **Dict[str, int]** |  | [optional] 
**spells** | [**List[MonsterGradeSpellsInner]**](MonsterGradeSpellsInner.md) | Spells assigned to this exact monster grade. | 

## Example

```python
from dofusdude.models.monster_grade import MonsterGrade

# TODO update the JSON string below
json = "{}"
# create an instance of MonsterGrade from a JSON string
monster_grade_instance = MonsterGrade.from_json(json)
# print the JSON string representation of the object
print(MonsterGrade.to_json())

# convert the object into a dict
monster_grade_dict = monster_grade_instance.to_dict()
# create an instance of MonsterGrade from a dict
monster_grade_from_dict = MonsterGrade.from_dict(monster_grade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


