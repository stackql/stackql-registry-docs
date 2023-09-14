---
title: webhook_delivery
hide_title: false
hide_table_of_contents: false
keywords:
  - webhook_delivery
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>webhook_delivery</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.webhook_delivery</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the delivery. |
| `repository_id` | `integer` | The id of the repository associated with this event. |
| `guid` | `string` | Unique identifier for the event (shared with all deliveries for all webhooks that subscribe to this event). |
| `event` | `string` | The event that triggered the delivery. |
| `status` | `string` | Description of the status of the attempted delivery |
| `url` | `string` | The URL target of the delivery. |
| `redelivery` | `boolean` | Whether the delivery is a redelivery. |
| `response` | `object` |  |
| `action` | `string` | The type of activity for the event that triggered the delivery. |
| `duration` | `number` | Time spent delivering. |
| `request` | `object` |  |
| `status_code` | `integer` | Status code received when delivery was made. |
| `installation_id` | `integer` | The id of the GitHub App installation associated with this event. |
| `delivered_at` | `string` | Time when the delivery was delivered. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_webhook_delivery` | `SELECT` | `delivery_id, hook_id, org` | Returns a delivery for a webhook configured in an organization. |
| `redeliver_webhook_delivery` | `EXEC` | `delivery_id, hook_id, org` | Redeliver a delivery for a webhook configured in an organization. |
