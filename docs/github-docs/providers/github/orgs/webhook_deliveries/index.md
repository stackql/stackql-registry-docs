---
title: webhook_deliveries
hide_title: false
hide_table_of_contents: false
keywords:
  - webhook_deliveries
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
<tr><td><b>Name</b></td><td><code>webhook_deliveries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.webhook_deliveries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the webhook delivery. |
| `redelivery` | `boolean` | Whether the webhook delivery is a redelivery. |
| `repository_id` | `integer` | The id of the repository associated with this event. |
| `status_code` | `integer` | Status code received when delivery was made. |
| `action` | `string` | The type of activity for the event that triggered the delivery. |
| `duration` | `number` | Time spent delivering. |
| `status` | `string` | Describes the response returned after attempting the delivery. |
| `event` | `string` | The event that triggered the delivery. |
| `guid` | `string` | Unique identifier for the event (shared with all deliveries for all webhooks that subscribe to this event). |
| `delivered_at` | `string` | Time when the webhook delivery occurred. |
| `installation_id` | `integer` | The id of the GitHub App installation associated with this event. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_webhook_deliveries` | `SELECT` | `hook_id, org` |
