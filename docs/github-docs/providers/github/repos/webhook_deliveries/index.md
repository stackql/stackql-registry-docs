---
title: webhook_deliveries
hide_title: false
hide_table_of_contents: false
keywords:
  - webhook_deliveries
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>webhook_deliveries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.webhook_deliveries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the delivery. |
| `action` | `string` | The type of activity for the event that triggered the delivery. |
| `delivered_at` | `string` | Time when the delivery was delivered. |
| `redelivery` | `boolean` | Whether the delivery is a redelivery. |
| `repository_id` | `integer` | The id of the repository associated with this event. |
| `status` | `string` | Description of the status of the attempted delivery |
| `duration` | `number` | Time spent delivering. |
| `status_code` | `integer` | Status code received when delivery was made. |
| `response` | `object` |  |
| `event` | `string` | The event that triggered the delivery. |
| `url` | `string` | The URL target of the delivery. |
| `installation_id` | `integer` | The id of the GitHub App installation associated with this event. |
| `guid` | `string` | Unique identifier for the event (shared with all deliveries for all webhooks that subscribe to this event). |
| `request` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_webhook_delivery` | `SELECT` | `delivery_id, hook_id, owner, repo` | Returns a delivery for a webhook configured in a repository. |
| `list_webhook_deliveries` | `SELECT` | `hook_id, owner, repo` | Returns a list of webhook deliveries for a webhook configured in a repository. |
| `redeliver_webhook_delivery` | `EXEC` | `delivery_id, hook_id, owner, repo` | Redeliver a webhook delivery for a webhook configured in a repository. |
