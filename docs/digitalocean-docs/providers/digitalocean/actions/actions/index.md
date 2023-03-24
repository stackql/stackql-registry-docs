---
title: actions
hide_title: false
hide_table_of_contents: false
keywords:
  - actions
  - actions
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.actions.actions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | A unique numeric ID that can be used to identify and reference an action. |
| `resource_type` | `string` | The type of resource that the action is associated with. |
| `status` | `string` | The current status of the action. This can be "in-progress", "completed", or "errored". |
| `resource_id` | `integer` | A unique identifier for the resource that the action is associated with. |
| `completed_at` | `string` | A time value given in ISO8601 combined date and time format that represents when the action was completed. |
| `type` | `string` | This is the type of action that the object represents. For example, this could be "transfer" to represent the state of an image transfer action. |
| `started_at` | `string` | A time value given in ISO8601 combined date and time format that represents when the action was initiated. |
| `region` | `object` |  |
| `region_slug` | `string` | A human-readable string that is used as a unique identifier for each region. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `action_id` | To retrieve a specific action object, send a GET request to `/v2/actions/$ACTION_ID`. |
| `list` | `SELECT` |  | This will be the entire list of actions taken on your account, so it will be quite large. As with any large collection returned by the API, the results will be paginated with only 20 on each page by default. |
| `_get` | `EXEC` | `action_id` | To retrieve a specific action object, send a GET request to `/v2/actions/$ACTION_ID`. |
| `_list` | `EXEC` |  | This will be the entire list of actions taken on your account, so it will be quite large. As with any large collection returned by the API, the results will be paginated with only 20 on each page by default. |
