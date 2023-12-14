---
title: webhooks
hide_title: false
hide_table_of_contents: false
keywords:
  - webhooks
  - webhooks
  - vercel    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Vercel resources using SQL
custom_edit_url: null
image: /img/providers/vercel/stackql-vercel-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>webhooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>vercel.webhooks.webhooks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The webhook id |
| `createdAt` | `number` | A number containing the date when the webhook was created in in milliseconds |
| `events` | `array` | The webhooks events |
| `ownerId` | `string` | The unique ID of the team the webhook belongs to |
| `projectIds` | `array` | The ID of the projects the webhook is associated with |
| `updatedAt` | `number` | A number containing the date when the webhook was updated in in milliseconds |
| `url` | `string` | A string with the URL of the webhook |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_webhook` | `SELECT` | `id, teamId` | Get a webhook |
| `get_webhooks` | `SELECT` | `teamId` | Get a list of webhooks |
| `create_webhook` | `INSERT` | `teamId, data__events, data__url` | Creates a webhook |
| `delete_webhook` | `DELETE` | `id, teamId` | Deletes a webhook |
