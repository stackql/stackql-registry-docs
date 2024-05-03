---
title: webhooks
hide_title: false
hide_table_of_contents: false
keywords:
  - webhooks
  - orgs
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>webhooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.orgs.webhooks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `integer` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="active" /> | `boolean` |
| <CopyableCode code="config" /> | `object` |
| <CopyableCode code="created_at" /> | `string` |
| <CopyableCode code="deliveries_url" /> | `string` |
| <CopyableCode code="events" /> | `array` |
| <CopyableCode code="ping_url" /> | `string` |
| <CopyableCode code="type" /> | `string` |
| <CopyableCode code="updated_at" /> | `string` |
| <CopyableCode code="url" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_webhook" /> | `SELECT` | <CopyableCode code="hook_id, org" /> | Returns a webhook configured in an organization. To get only the webhook `config` properties, see "[Get a webhook configuration for an organization](/rest/orgs/webhooks#get-a-webhook-configuration-for-an-organization)." |
| <CopyableCode code="list_webhooks" /> | `SELECT` | <CopyableCode code="org" /> |  |
| <CopyableCode code="create_webhook" /> | `INSERT` | <CopyableCode code="org, data__config, data__name" /> | Here's how you can create a hook that posts payloads in JSON format: |
| <CopyableCode code="delete_webhook" /> | `DELETE` | <CopyableCode code="hook_id, org" /> |  |
| <CopyableCode code="ping_webhook" /> | `EXEC` | <CopyableCode code="hook_id, org" /> | This will trigger a [ping event](https://docs.github.com/webhooks/#ping-event) to be sent to the hook. |
| <CopyableCode code="update_webhook" /> | `EXEC` | <CopyableCode code="hook_id, org" /> | Updates a webhook configured in an organization. When you update a webhook, the `secret` will be overwritten. If you previously had a `secret` set, you must provide the same `secret` or set a new `secret` or the secret will be removed. If you are only updating individual webhook `config` properties, use "[Update a webhook configuration for an organization](/rest/orgs/webhooks#update-a-webhook-configuration-for-an-organization)." |
