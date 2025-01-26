# coding: utf-8

"""
    dofusdude

    # Open Ankama Developer Community The all-in-one toolbelt for your next Ankama related project.  ## Versions - [Dofus 2](https://docs.dofusdu.de/dofus2/) - [Dofus 3](https://docs.dofusdu.de/dofus3/)   - v1 [latest] (you are here)   ## Client SDKs - [Javascript](https://github.com/dofusdude/dofusdude-js) `npm i dofusdude-js --save` - [Typescript](https://github.com/dofusdude/dofusdude-ts) `npm i dofusdude-ts --save` - [Go](https://github.com/dofusdude/dodugo) `go get -u github.com/dofusdude/dodugo` - [Python](https://github.com/dofusdude/dofusdude-py) `pip install dofusdude` - [Java](https://github.com/dofusdude/dofusdude-java) Maven with GitHub packages setup  Everything, including this site, is generated out of the [Docs Repo](https://github.com/dofusdude/api-docs). Consider it the Single Source of Truth. If there is a problem with the SDKs, create an issue there.  Your favorite language is missing? Please let me know!  # Main Features - 🥷 **Seamless Auto-Update** load data in the background when a new Dofus version is released and serving it within 10 minutes with atomic data source switching. No downtime and no effects for the user, just always up-to-date.  - ⚡ **Blazingly Fast** all data in-memory, aggressive caching over short time spans, HTTP/2 multiplexing, written in Go, optimized for low latency, hosted on bare metal in 🇩🇪.  - 📨 **Almanax Discord Integration** Use the endpoints as a dev or the official [Web Client](https://discord.dofusdude.com) as a user.  - 🩸 **Dofus 3 Beta** from stable to bleeding edge by replacing /dofus3 with /dofus3beta.  - 🗣️ **Multilingual** supporting _en_, _fr_, _es_, _pt_, _de_.  - 🧠 **Search by Relevance** allowing typos in name and description, handled by language specific text analysis and indexing.  - 🕵️ **Official Sources** generated from actual data from the game.  ... and much more on the Roadmap on my [Discord](https://discord.gg/3EtHskZD8h). 

    The version of the OpenAPI document: 1.0.0-rc.10
    Contact: stelzo@steado.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dofusdude.models.equipment import Equipment

class TestEquipment(unittest.TestCase):
    """Equipment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Equipment:
        """Test Equipment
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Equipment`
        """
        model = Equipment()
        if include_optional:
            return Equipment(
                ankama_id = 56,
                name = '',
                description = '',
                type = dofusdude.models.translated_id.TranslatedId(
                    id = 56, 
                    name = '', ),
                is_weapon = True,
                level = 56,
                pods = 56,
                image_urls = dofusdude.models.images.Images(
                    icon = '', 
                    sd = '', 
                    hq = '', 
                    hd = '', ),
                effects = [
                    dofusdude.models.effect.Effect(
                        int_minimum = 56, 
                        int_maximum = 56, 
                        type = dofusdude.models.effect_type.EffectType(
                            id = 56, 
                            name = '', 
                            is_active = True, 
                            is_meta = True, ), 
                        ignore_int_min = True, 
                        ignore_int_max = True, 
                        formatted = '', )
                    ],
                conditions = None,
                recipe = [
                    dofusdude.models.recipe.Recipe(
                        item_ankama_id = 56, 
                        item_subtype = '', 
                        quantity = 56, )
                    ],
                parent_set = dofusdude.models.translated_id.TranslatedId(
                    id = 56, 
                    name = '', )
            )
        else:
            return Equipment(
        )
        """

    def testEquipment(self):
        """Test Equipment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
