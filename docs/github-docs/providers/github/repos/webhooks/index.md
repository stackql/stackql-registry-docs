---
title: webhooks
hide_title: false
hide_table_of_contents: false
keywords:
  - webhooks
  - repos
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
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.webhooks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | Unique identifier of the webhook. |
| <CopyableCode code="name" /> | `string` | The name of a valid service, use 'web' for a webhook. |
| <CopyableCode code="active" /> | `boolean` | Determines whether the hook is actually triggered on pushes. |
| <CopyableCode code="config" /> | `object` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="deliveries_url" /> | `string` |  |
| <CopyableCode code="events" /> | `array` | Determines what events the hook is triggered for. Default: ['push']. |
| <CopyableCode code="last_response" /> | `object` |  |
| <CopyableCode code="ping_url" /> | `string` |  |
| <CopyableCode code="test_url" /> | `string` |  |
| <CopyableCode code="type" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_webhook" /> | `SELECT` | <CopyableCode code="hook_id, owner, repo" /> | Returns a webhook configured in a repository. To get only the webhook `config` properties, see "[Get a webhook configuration for a repository](/rest/webhooks/repo-config#get-a-webhook-configuration-for-a-repository)." |
| <CopyableCode code="list_webhooks" /> | `SELECT` | <CopyableCode code="owner, repo" /> | Lists webhooks for a repository. `last response` may return null if there have not been any deliveries within 30 days. |
| <CopyableCode code="create_webhook" /> | `INSERT` | <CopyableCode code="owner, repo" /> | Repositories can have multiple webhooks installed. Each webhook should have a unique `config`. Multiple webhooks can<br />share the same `config` as long as those webhooks do not have any `events` that overlap. |
| <CopyableCode code="delete_webhook" /> | `DELETE` | <CopyableCode code="hook_id, owner, repo" /> |  |
| <CopyableCode code="ping_webhook" /> | `EXEC` | <CopyableCode code="hook_id, owner, repo" /> | This will trigger a [ping event](https://docs.github.com/webhooks/#ping-event) to be sent to the hook. |
| <CopyableCode code="test_push_webhook" /> | `EXEC` | <CopyableCode code="hook_id, owner, repo" /> | This will trigger the hook with the latest push to the current repository if the hook is subscribed to `push` events. If the hook is not subscribed to `push` events, the server will respond with 204 but no test POST will be generated.<br /><br />**Note**: Previously `/repos/:owner/:repo/hooks/:hook_id/test` |
| <CopyableCode code="update_webhook" /> | `EXEC` | <CopyableCode code="hook_id, owner, repo" /> | Updates a webhook configured in a repository. If you previously had a `secret` set, you must provide the same `secret` or set a new `secret` or the secret will be removed. If you are only updating individual webhook `config` properties, use "[Update a webhook configuration for a repository](/rest/webhooks/repo-config#update-a-webhook-configuration-for-a-repository)." |
