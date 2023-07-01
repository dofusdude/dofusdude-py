# coding: utf-8

"""
    Dofusdude

    # A project for you - the developer. The free, always-up-to-date, low-latency, insert-buzzword-here Ankama API for your next cool project!  ## Client SDKs Don't write types or functions yourself - I already (kinda) did! 😉 - [Javascript](https://github.com/dofusdude/dofusdude-js) npm i dofusdude-js --save - [Typescript](https://github.com/dofusdude/dofusdude-ts) npm i dofusdude-ts --save - [Go](https://github.com/dofusdude/dodugo) go get -u github.com/dofusdude/dodugo - [Python](https://github.com/dofusdude/dofusdude-py) pip install dofusdude - [PHP](https://github.com/dofusdude/dofusdude-php)  Everything, including this site, is generated out of the [Docs Repo](https://github.com/dofusdude/api-docs). Consider it the Single Source of Truth. If there is a problem with the SDKs, create an issue there.  Your favorite language is missing? Please let me know!  # Main Features - 🥷 **Seamless Auto-Update** load data in the background when a new Dofus version is released and serving it within 2 minutes with atomic data source switching. No downtime and no effects for the user, just always up-to-date.  - ⚡ **Blazingly Fast** all data in-memory, aggressive caching over short time spans, HTTP/2 multiplexing, written in Go, optimized for low latency, hosted on bare metal in 🇩🇪.  - 📨 **Discord Integration** Ankama related Twitter, RSS and Almanax feeds to post to Discord servers with advanced features like filters or mentions. Use the endpoints as a dev or the official [Web Client](https://discord.dofusdude.com) as a user.  - 🩸 **Dofus 2 Beta** from stable to bleeding edge by replacing /dofus2 with /dofus2beta.  - 🗣️ **Multilingual** supporting _en_, _fr_, _es_, _pt_ including the dropped languages from the Dofus website _de_ and _it_.  - 🧠 **Search by Relevance** allowing typos in name and description, handled by language specific text analysis and indexing by the powerful [Meilisearch](https://www.meilisearch.com) written in Rust.  - 🕵️ **Complete** actual data from the game including items invisible to the encyclopedia like quest items.  - 🖼️ **HD Images** rendering vector graphics into PNGs up to 800x800 px in the background.   ## Current state - Weapons ✅ - Equipment ✅ - Sets ✅ - Resources ✅ - Consumables ✅ - Pets ✅ - Mounts ✅ - Cosmetics/Ceremonial Items ✅ - Harnesses ✅ - Quest Items ✅ - Almanax ✅ - Monsters ❌ - Spells ❌  ... and much more on the Roadmap on my Discord.   ## Deploy now. Use forever. Everything you see here on this site, you can use now and forever. Updates could introduce new fields, new paths or parameter but never break backwards compatibility, so no field or parameter will be deleted.  There is one exception! **The API will _always_ choose being up-to-date over everything else**. So if Ankama decides to drop languages from the game like they did with their website, the API will loose support for them, too.  ## Only the beginning... 🤯 I want this project to be useful and not just add plain GET-categories no one needs.  There is a long list of features I want to add (see the Roadmap on my [Discord](https://discord.gg/3EtHskZD8h)). But they are all focussed on you, the developers. So please let me know what you need. I will change the list based on demand.  # Get started! 🥳 Scroll down and try it for yourself!  Or see how these other awesome projects use it: - [KaellyBot](https://github.com/Kaysoro/KaellyBot) by Kaysoro - [Dofus Craftlist](https://dofuscraftlist-dev.netlify.app) by Lystina - [AlmanaxApp](https://almanaxapp.netlify.app) by Lystina - [DofuStuffSimulator](https://dofusstuffsimulator.netlify.app/)  I highly recommend using the SDKs for quick results. I use them myself for parts of the API.  ## Thank you! I highly welcome everyone on my [Discord](https://discord.gg/3EtHskZD8h) to just talk about projects and use cases or give feedback of any kind.  The servers have a fixed monthly cost to provide very fast responses. If you want to help me keeping them running or simply  donate, consider becoming a [GitHub Sponsor](https://github.com/sponsors/dofusdude).   # noqa: E501

    The version of the OpenAPI document: 0.7.2
    Contact: stelzo@steado.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, validator
from dofusdude.models.create_almanax_webhook_daily_settings import CreateAlmanaxWebhookDailySettings
from dofusdude.models.create_almanax_webhook_mentions_value_inner import CreateAlmanaxWebhookMentionsValueInner

class PutAlmanaxWebhook(BaseModel):
    """
    PutAlmanaxWebhook
    """
    bonus_whitelist: Optional[conlist(StrictStr)] = Field(None, description="from all available bonuses (ids) from /dofus2/meta/{language}/almanax/bonuses. Delete old entries with empty array []. Just null changes nothing.")
    bonus_blacklist: Optional[conlist(StrictStr)] = Field(None, description="from all available bonuses (ids) from /dofus2/meta/{language}/almanax/bonuses. Delete old entries with empty array []. Just null changes nothing.")
    subscriptions: Optional[conlist(StrictStr)] = Field(None, description="Get the available subscriptions with /meta/webhooks/almanax")
    daily_settings: Optional[CreateAlmanaxWebhookDailySettings] = None
    iso_date: Optional[StrictBool] = Field(False, description="If false, it will use common local time formats and weekday translations. If true, the format is YYYY-MM-DD.")
    mentions: Optional[Dict[str, conlist(CreateAlmanaxWebhookMentionsValueInner)]] = Field(None, description="Almanax bonus ids mapped to array of mentions.")
    intervals: Optional[conlist(StrictStr, unique_items=True)] = None
    weekly_weekday: Optional[StrictStr] = Field(None, description="When to post the weekly preview at the specified time.")
    __properties = ["bonus_whitelist", "bonus_blacklist", "subscriptions", "daily_settings", "iso_date", "mentions", "intervals", "weekly_weekday"]

    @validator('intervals')
    def intervals_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ('daily', 'weekly', 'monthly'):
                raise ValueError("each list item must be one of ('daily', 'weekly', 'monthly')")
        return value

    @validator('weekly_weekday')
    def weekly_weekday_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'):
            raise ValueError("must be one of enum values ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> PutAlmanaxWebhook:
        """Create an instance of PutAlmanaxWebhook from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of daily_settings
        if self.daily_settings:
            _dict['daily_settings'] = self.daily_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in mentions (dict of array)
        _field_dict_of_array = {}
        if self.mentions:
            for _key in self.mentions:
                if self.mentions[_key]:
                    _field_dict_of_array[_key] = [
                        _item.to_dict() for _item in self.mentions[_key]
                    ]
            _dict['mentions'] = _field_dict_of_array
        # set to None if bonus_whitelist (nullable) is None
        # and __fields_set__ contains the field
        if self.bonus_whitelist is None and "bonus_whitelist" in self.__fields_set__:
            _dict['bonus_whitelist'] = None

        # set to None if bonus_blacklist (nullable) is None
        # and __fields_set__ contains the field
        if self.bonus_blacklist is None and "bonus_blacklist" in self.__fields_set__:
            _dict['bonus_blacklist'] = None

        # set to None if subscriptions (nullable) is None
        # and __fields_set__ contains the field
        if self.subscriptions is None and "subscriptions" in self.__fields_set__:
            _dict['subscriptions'] = None

        # set to None if daily_settings (nullable) is None
        # and __fields_set__ contains the field
        if self.daily_settings is None and "daily_settings" in self.__fields_set__:
            _dict['daily_settings'] = None

        # set to None if iso_date (nullable) is None
        # and __fields_set__ contains the field
        if self.iso_date is None and "iso_date" in self.__fields_set__:
            _dict['iso_date'] = None

        # set to None if intervals (nullable) is None
        # and __fields_set__ contains the field
        if self.intervals is None and "intervals" in self.__fields_set__:
            _dict['intervals'] = None

        # set to None if weekly_weekday (nullable) is None
        # and __fields_set__ contains the field
        if self.weekly_weekday is None and "weekly_weekday" in self.__fields_set__:
            _dict['weekly_weekday'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PutAlmanaxWebhook:
        """Create an instance of PutAlmanaxWebhook from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PutAlmanaxWebhook.parse_obj(obj)

        _obj = PutAlmanaxWebhook.parse_obj({
            "bonus_whitelist": obj.get("bonus_whitelist"),
            "bonus_blacklist": obj.get("bonus_blacklist"),
            "subscriptions": obj.get("subscriptions"),
            "daily_settings": CreateAlmanaxWebhookDailySettings.from_dict(obj.get("daily_settings")) if obj.get("daily_settings") is not None else None,
            "iso_date": obj.get("iso_date") if obj.get("iso_date") is not None else False,
            "mentions": dict(
                (_k,
                        [CreateAlmanaxWebhookMentionsValueInner.from_dict(_item) for _item in _v]
                        if _v is not None
                        else None
                )
                for _k, _v in obj.get("mentions").items()
            ),
            "intervals": obj.get("intervals"),
            "weekly_weekday": obj.get("weekly_weekday")
        })
        return _obj

