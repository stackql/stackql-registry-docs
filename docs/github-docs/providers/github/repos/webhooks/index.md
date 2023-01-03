---
title: webhooks
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>webhooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.webhooks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the webhook. |
| `name` | `string` | The name of a valid service, use 'web' for a webhook. |
| `ping_url` | `string` |  |
| `deliveries_url` | `string` |  |
| `url` | `string` |  |
| `test_url` | `string` |  |
| `created_at` | `string` |  |
| `events` | `array` | Determines what events the hook is triggered for. Default: ['push']. |
| `active` | `boolean` | Determines whether the hook is actually triggered on pushes. |
| `updated_at` | `string` |  |
| `config` | `object` |  |
| `type` | `string` |  |
| `last_response` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_webhook` | `SELECT` | `hook_id, owner, repo` | Returns a webhook configured in a repository. To get only the webhook `config` properties, see "[Get a webhook configuration for a repository](https://docs.github.com/en/rest/webhooks/repo-config#get-a-webhook-configuration-for-a-repository)." |
| `list_webhooks` | `SELECT` | `owner, repo` |  |
| `create_webhook` | `INSERT` | `owner, repo` | Repositories can have multiple webhooks installed. Each webhook should have a unique `config`. Multiple webhooks can<br />share the same `config` as long as those webhooks do not have any `events` that overlap. |
| `delete_webhook` | `DELETE` | `hook_id, owner, repo` |  |
| `ping_webhook` | `EXEC` | `hook_id, owner, repo` | This will trigger a [ping event](https://docs.github.com/webhooks/#ping-event) to be sent to the hook. |
| `test_push_webhook` | `EXEC` | `hook_id, owner, repo` | This will trigger the hook with the latest push to the current repository if the hook is subscribed to `push` events. If the hook is not subscribed to `push` events, the server will respond with 204 but no test POST will be generated.<br /><br />**Note**: Previously `/repos/:owner/:repo/hooks/:hook_id/test` |
| `update_webhook` | `EXEC` | `hook_id, owner, repo` | Updates a webhook configured in a repository. If you previously had a `secret` set, you must provide the same `secret` or set a new `secret` or the secret will be removed. If you are only updating individual webhook `config` properties, use "[Update a webhook configuration for a repository](https://docs.github.com/en/rest/webhooks/repo-config#update-a-webhook-configuration-for-a-repository)." |
