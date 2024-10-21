# coding: utf-8

"""
    dofusdude

    # A project for you - the developer. The all-in-one toolbelt for your next Ankama related project.  ## Client SDKs - [Javascript](https://github.com/dofusdude/dofusdude-js) `npm i dofusdude-js --save` - [Typescript](https://github.com/dofusdude/dofusdude-ts) `npm i dofusdude-ts --save` - [Go](https://github.com/dofusdude/dodugo) `go get -u github.com/dofusdude/dodugo` - [Python](https://github.com/dofusdude/dofusdude-py) `pip install dofusdude` - [PHP](https://github.com/dofusdude/dofusdude-php) - [Java](https://github.com/dofusdude/dofusdude-java) Maven with GitHub packages setup  Everything, including this site, is generated out of the [Docs Repo](https://github.com/dofusdude/api-docs). Consider it the Single Source of Truth. If there is a problem with the SDKs, create an issue there.  Your favorite language is missing? Please let me know!  # Main Features - 🥷 **Seamless Auto-Update** load data in the background when a new Dofus version is released and serving it within 10 minutes with atomic data source switching. No downtime and no effects for the user, just always up-to-date.  - ⚡ **Blazingly Fast** all data in-memory, aggressive caching over short time spans, HTTP/2 multiplexing, written in Go, optimized for low latency, hosted on bare metal in 🇩🇪.  - 📨 **Discord Integration** Ankama related RSS and Almanax feeds to post to Discord servers with advanced features like filters or mentions. Use the endpoints as a dev or the official [Web Client](https://discord.dofusdude.com) as a user.  - 🩸 **Dofus 2 Beta** from stable to bleeding edge by replacing /dofus2 with /dofus2beta.  - 🗣️ **Multilingual** supporting _en_, _fr_, _es_, _pt_ including the dropped languages from the Dofus website _de_ and _it_.  - 🧠 **Search by Relevance** allowing typos in name and description, handled by language specific text analysis and indexing.  - 🕵️ **Complete** actual data from the game including items invisible to the encyclopedia like quest items.  - 🖼️ **HD Images** rendering game assets to high-res images with up to 800x800 px.  ... and much more on the Roadmap on my [Discord](https://discord.gg/3EtHskZD8h). 

    The version of the OpenAPI document: 0.9.4
    Contact: stelzo@steado.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from dofusdude.models.create_almanax_webhook_daily_settings import CreateAlmanaxWebhookDailySettings
from dofusdude.models.create_almanax_webhook_mentions_value_inner import CreateAlmanaxWebhookMentionsValueInner
from typing import Optional, Set
from typing_extensions import Self

class PutAlmanaxWebhook(BaseModel):
    """
    PutAlmanaxWebhook
    """ # noqa: E501
    bonus_whitelist: Optional[List[StrictStr]] = Field(default=None, description="from all available bonuses (ids) from /dofus2/meta/{language}/almanax/bonuses. Delete old entries with empty array []. Just null changes nothing.")
    bonus_blacklist: Optional[List[StrictStr]] = Field(default=None, description="from all available bonuses (ids) from /dofus2/meta/{language}/almanax/bonuses. Delete old entries with empty array []. Just null changes nothing.")
    subscriptions: Optional[List[StrictStr]] = Field(default=None, description="Get the available subscriptions with /meta/webhooks/almanax")
    daily_settings: Optional[CreateAlmanaxWebhookDailySettings] = None
    iso_date: Optional[StrictBool] = Field(default=False, description="If false, it will use common local time formats and weekday translations. If true, the format is YYYY-MM-DD.")
    mentions: Optional[Dict[str, List[CreateAlmanaxWebhookMentionsValueInner]]] = Field(default=None, description="Almanax bonus ids mapped to array of mentions.")
    intervals: Optional[List[StrictStr]] = None
    weekly_weekday: Optional[StrictStr] = Field(default=None, description="When to post the weekly preview at the specified time.")
    __properties: ClassVar[List[str]] = ["bonus_whitelist", "bonus_blacklist", "subscriptions", "daily_settings", "iso_date", "mentions", "intervals", "weekly_weekday"]

    @field_validator('intervals')
    def intervals_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['daily', 'weekly', 'monthly']):
                raise ValueError("each list item must be one of ('daily', 'weekly', 'monthly')")
        return value

    @field_validator('weekly_weekday')
    def weekly_weekday_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']):
            raise ValueError("must be one of enum values ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')")
        return value

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
        """Create an instance of PutAlmanaxWebhook from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of daily_settings
        if self.daily_settings:
            _dict['daily_settings'] = self.daily_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in mentions (dict of array)
        _field_dict_of_array = {}
        if self.mentions:
            for _key_mentions in self.mentions:
                if self.mentions[_key_mentions] is not None:
                    _field_dict_of_array[_key_mentions] = [
                        _item.to_dict() for _item in self.mentions[_key_mentions]
                    ]
            _dict['mentions'] = _field_dict_of_array
        # set to None if bonus_whitelist (nullable) is None
        # and model_fields_set contains the field
        if self.bonus_whitelist is None and "bonus_whitelist" in self.model_fields_set:
            _dict['bonus_whitelist'] = None

        # set to None if bonus_blacklist (nullable) is None
        # and model_fields_set contains the field
        if self.bonus_blacklist is None and "bonus_blacklist" in self.model_fields_set:
            _dict['bonus_blacklist'] = None

        # set to None if subscriptions (nullable) is None
        # and model_fields_set contains the field
        if self.subscriptions is None and "subscriptions" in self.model_fields_set:
            _dict['subscriptions'] = None

        # set to None if daily_settings (nullable) is None
        # and model_fields_set contains the field
        if self.daily_settings is None and "daily_settings" in self.model_fields_set:
            _dict['daily_settings'] = None

        # set to None if iso_date (nullable) is None
        # and model_fields_set contains the field
        if self.iso_date is None and "iso_date" in self.model_fields_set:
            _dict['iso_date'] = None

        # set to None if intervals (nullable) is None
        # and model_fields_set contains the field
        if self.intervals is None and "intervals" in self.model_fields_set:
            _dict['intervals'] = None

        # set to None if weekly_weekday (nullable) is None
        # and model_fields_set contains the field
        if self.weekly_weekday is None and "weekly_weekday" in self.model_fields_set:
            _dict['weekly_weekday'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PutAlmanaxWebhook from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bonus_whitelist": obj.get("bonus_whitelist"),
            "bonus_blacklist": obj.get("bonus_blacklist"),
            "subscriptions": obj.get("subscriptions"),
            "daily_settings": CreateAlmanaxWebhookDailySettings.from_dict(obj["daily_settings"]) if obj.get("daily_settings") is not None else None,
            "iso_date": obj.get("iso_date") if obj.get("iso_date") is not None else False,
            "mentions": dict(
                (_k,
                        [CreateAlmanaxWebhookMentionsValueInner.from_dict(_item) for _item in _v]
                        if _v is not None
                        else None
                )
                for _k, _v in obj.get("mentions", {}).items()
            ),
            "intervals": obj.get("intervals"),
            "weekly_weekday": obj.get("weekly_weekday")
        })
        return _obj


