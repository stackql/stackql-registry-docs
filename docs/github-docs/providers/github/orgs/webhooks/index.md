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
<tr><td><b>Id</b></td><td><code>github.orgs.webhooks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `created_at` | `string` |
| `ping_url` | `string` |
| `url` | `string` |
| `events` | `array` |
| `updated_at` | `string` |
| `config` | `object` |
| `deliveries_url` | `string` |
| `type` | `string` |
| `active` | `boolean` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_webhook` | `SELECT` | `hook_id, org` | Returns a webhook configured in an organization. To get only the webhook `config` properties, see "[Get a webhook configuration for an organization](https://docs.github.com/en/rest/orgs/webhooks#get-a-webhook-configuration-for-an-organization)." |
| `list_webhooks` | `SELECT` | `org` |  |
| `create_webhook` | `INSERT` | `org, data__config, data__name` | Here's how you can create a hook that posts payloads in JSON format: |
| `delete_webhook` | `DELETE` | `hook_id, org` |  |
| `ping_webhook` | `EXEC` | `hook_id, org` | This will trigger a [ping event](https://docs.github.com/webhooks/#ping-event) to be sent to the hook. |
| `update_webhook` | `EXEC` | `hook_id, org` | Updates a webhook configured in an organization. When you update a webhook, the `secret` will be overwritten. If you previously had a `secret` set, you must provide the same `secret` or set a new `secret` or the secret will be removed. If you are only updating individual webhook `config` properties, use "[Update a webhook configuration for an organization](https://docs.github.com/en/rest/orgs/webhooks#update-a-webhook-configuration-for-an-organization)." |
