---
title: events
hide_title: false
hide_table_of_contents: false
keywords:
  - events
  - user
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
<tr><td><b>Name</b></td><td><code>events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>vercel.user.events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique identifier of the Event. |
| `createdAt` | `number` | Timestamp (in milliseconds) of when the event was generated. |
| `entities` | `array` | A list of "entities" within the event `text`. Useful for enhancing the displayed text with additional styling and links. |
| `text` | `string` | The human-readable text of the Event. |
| `user` | `object` | Metadata for the User who generated the event. |
| `userId` | `string` | The unique identifier of the User who generated the event. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_user_events` | `SELECT` | `teamId` |
| `_list_user_events` | `EXEC` | `teamId` |
