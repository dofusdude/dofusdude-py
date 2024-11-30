# coding: utf-8

"""
    dofusdude

    # Open Ankama Developer Community The all-in-one toolbelt for your next Ankama related project.  ## Versions - [Dofus 2](https://docs.dofusdu.de/dofus2/) - [Dofus 3](https://docs.dofusdu.de/dofus3/)   - v1 [latest] (you are here)   ## Client SDKs - [Javascript](https://github.com/dofusdude/dofusdude-js) `npm i dofusdude-js --save` - [Typescript](https://github.com/dofusdude/dofusdude-ts) `npm i dofusdude-ts --save` - [Go](https://github.com/dofusdude/dodugo) `go get -u github.com/dofusdude/dodugo` - [Python](https://github.com/dofusdude/dofusdude-py) `pip install dofusdude` - [Java](https://github.com/dofusdude/dofusdude-java) Maven with GitHub packages setup  Everything, including this site, is generated out of the [Docs Repo](https://github.com/dofusdude/api-docs). Consider it the Single Source of Truth. If there is a problem with the SDKs, create an issue there.  Your favorite language is missing? Please let me know!  # Main Features - 🥷 **Seamless Auto-Update** load data in the background when a new Dofus version is released and serving it within 10 minutes with atomic data source switching. No downtime and no effects for the user, just always up-to-date.  - ⚡ **Blazingly Fast** all data in-memory, aggressive caching over short time spans, HTTP/2 multiplexing, written in Go, optimized for low latency, hosted on bare metal in 🇩🇪.  - 📨 **Almanax Discord Integration** Use the endpoints as a dev or the official [Web Client](https://discord.dofusdude.com) as a user.  - 🩸 **Dofus 3 Beta** from stable to bleeding edge by replacing /dofus3 with /dofus3beta.  - 🗣️ **Multilingual** supporting _en_, _fr_, _es_, _pt_, _de_.  - 🧠 **Search by Relevance** allowing typos in name and description, handled by language specific text analysis and indexing.  - 🕵️ **Official Sources** generated from actual data from the game.  ... and much more on the Roadmap on my [Discord](https://discord.gg/3EtHskZD8h). 

    The version of the OpenAPI document: 1.0.0-rc.5
    Contact: stelzo@steado.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dofusdude.models.condition_node import ConditionNode
from dofusdude.models.effect import Effect
from dofusdude.models.images import Images
from dofusdude.models.range import Range
from dofusdude.models.recipe import Recipe
from dofusdude.models.translated_id import TranslatedId
from typing import Optional, Set
from typing_extensions import Self

class Weapon(BaseModel):
    """
    Weapon
    """ # noqa: E501
    ankama_id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    type: Optional[TranslatedId] = None
    is_weapon: Optional[StrictBool] = Field(default=None, description="always true when the item is a weapon. Many fields are now available. Always check for this flag first when getting single equipment items.")
    level: Optional[StrictInt] = None
    pods: Optional[StrictInt] = None
    image_urls: Optional[Images] = None
    effects: Optional[List[Effect]] = None
    conditions: Optional[ConditionNode] = None
    critical_hit_probability: Optional[StrictInt] = None
    critical_hit_bonus: Optional[StrictInt] = None
    max_cast_per_turn: Optional[StrictInt] = None
    ap_cost: Optional[StrictInt] = None
    range: Optional[Range] = None
    recipe: Optional[List[Recipe]] = None
    parent_set: Optional[TranslatedId] = None
    __properties: ClassVar[List[str]] = ["ankama_id", "name", "description", "type", "is_weapon", "level", "pods", "image_urls", "effects", "conditions", "critical_hit_probability", "critical_hit_bonus", "max_cast_per_turn", "ap_cost", "range", "recipe", "parent_set"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Weapon from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['type'] = self.type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of image_urls
        if self.image_urls:
            _dict['image_urls'] = self.image_urls.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in effects (list)
        _items = []
        if self.effects:
            for _item_effects in self.effects:
                if _item_effects:
                    _items.append(_item_effects.to_dict())
            _dict['effects'] = _items
        # override the default output from pydantic by calling `to_dict()` of conditions
        if self.conditions:
            _dict['conditions'] = self.conditions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of range
        if self.range:
            _dict['range'] = self.range.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in recipe (list)
        _items = []
        if self.recipe:
            for _item_recipe in self.recipe:
                if _item_recipe:
                    _items.append(_item_recipe.to_dict())
            _dict['recipe'] = _items
        # override the default output from pydantic by calling `to_dict()` of parent_set
        if self.parent_set:
            _dict['parent_set'] = self.parent_set.to_dict()
        # set to None if effects (nullable) is None
        # and model_fields_set contains the field
        if self.effects is None and "effects" in self.model_fields_set:
            _dict['effects'] = None

        # set to None if conditions (nullable) is None
        # and model_fields_set contains the field
        if self.conditions is None and "conditions" in self.model_fields_set:
            _dict['conditions'] = None

        # set to None if recipe (nullable) is None
        # and model_fields_set contains the field
        if self.recipe is None and "recipe" in self.model_fields_set:
            _dict['recipe'] = None

        # set to None if parent_set (nullable) is None
        # and model_fields_set contains the field
        if self.parent_set is None and "parent_set" in self.model_fields_set:
            _dict['parent_set'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Weapon from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ankama_id": obj.get("ankama_id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "type": TranslatedId.from_dict(obj["type"]) if obj.get("type") is not None else None,
            "is_weapon": obj.get("is_weapon"),
            "level": obj.get("level"),
            "pods": obj.get("pods"),
            "image_urls": Images.from_dict(obj["image_urls"]) if obj.get("image_urls") is not None else None,
            "effects": [Effect.from_dict(_item) for _item in obj["effects"]] if obj.get("effects") is not None else None,
            "conditions": ConditionNode.from_dict(obj["conditions"]) if obj.get("conditions") is not None else None,
            "critical_hit_probability": obj.get("critical_hit_probability"),
            "critical_hit_bonus": obj.get("critical_hit_bonus"),
            "max_cast_per_turn": obj.get("max_cast_per_turn"),
            "ap_cost": obj.get("ap_cost"),
            "range": Range.from_dict(obj["range"]) if obj.get("range") is not None else None,
            "recipe": [Recipe.from_dict(_item) for _item in obj["recipe"]] if obj.get("recipe") is not None else None,
            "parent_set": TranslatedId.from_dict(obj["parent_set"]) if obj.get("parent_set") is not None else None
        })
        return _obj


