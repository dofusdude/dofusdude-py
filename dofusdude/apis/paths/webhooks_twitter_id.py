from dofusdude.paths.webhooks_twitter_id.get import ApiForget
from dofusdude.paths.webhooks_twitter_id.put import ApiForput
from dofusdude.paths.webhooks_twitter_id.delete import ApiFordelete


class WebhooksTwitterId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
