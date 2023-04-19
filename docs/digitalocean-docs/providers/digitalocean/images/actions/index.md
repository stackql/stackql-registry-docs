---
title: actions
hide_title: false
hide_table_of_contents: false
keywords:
  - actions
  - images
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
<tr><td><b>Id</b></td><td><code>digitalocean.images.actions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | A unique numeric ID that can be used to identify and reference an action. |
| `region` | `object` |  |
| `resource_id` | `integer` | A unique identifier for the resource that the action is associated with. |
| `resource_type` | `string` | The type of resource that the action is associated with. |
| `type` | `string` | This is the type of action that the object represents. For example, this could be "transfer" to represent the state of an image transfer action. |
| `region_slug` | `string` | A human-readable string that is used as a unique identifier for each region. |
| `status` | `string` | The current status of the action. This can be "in-progress", "completed", or "errored". |
| `completed_at` | `string` | A time value given in ISO8601 combined date and time format that represents when the action was completed. |
| `started_at` | `string` | A time value given in ISO8601 combined date and time format that represents when the action was initiated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `imageActions_get` | `SELECT` | `action_id, image_id` | To retrieve the status of an image action, send a GET request to `/v2/images/$IMAGE_ID/actions/$IMAGE_ACTION_ID`. |
| `imageActions_list` | `SELECT` | `image_id` | To retrieve all actions that have been executed on an image, send a GET request to `/v2/images/$IMAGE_ID/actions`. |
| `imageActions_post` | `INSERT` | `image_id` | The following actions are available on an Image.<br /><br />## Convert an Image to a Snapshot<br /><br />To convert an image, for example, a backup to a snapshot, send a POST request<br />to `/v2/images/$IMAGE_ID/actions`. Set the `type` attribute to `convert`.<br /><br />## Transfer an Image<br /><br />To transfer an image to another region, send a POST request to<br />`/v2/images/$IMAGE_ID/actions`. Set the `type` attribute to `transfer` and set<br />`region` attribute to the slug identifier of the region you wish to transfer<br />to.<br /> |
| `_imageActions_get` | `EXEC` | `action_id, image_id` | To retrieve the status of an image action, send a GET request to `/v2/images/$IMAGE_ID/actions/$IMAGE_ACTION_ID`. |
| `_imageActions_list` | `EXEC` | `image_id` | To retrieve all actions that have been executed on an image, send a GET request to `/v2/images/$IMAGE_ID/actions`. |
