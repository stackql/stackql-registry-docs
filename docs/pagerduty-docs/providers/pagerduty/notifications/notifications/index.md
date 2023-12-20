---
title: notifications
hide_title: false
hide_table_of_contents: false
keywords:
  - notifications
  - notifications
  - pagerduty    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, manage, and integrate PagerDuty resources using SQL
custom_edit_url: null
image: /img/providers/pagerduty/stackql-pagerduty-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notifications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.notifications.notifications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `` | `string` |  |
| `address` | `string` | The address where the notification was sent. This will be null for notification type `push_notification`. |
| `conferenceAddress` | `string` | The address of the conference bridge |
| `started_at` | `string` | The time at which the notification was sent |
| `status` | `string` |  |
| `type` | `string` | The type of notification. |
| `user` | `object` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_notifications` | `SELECT` | `since, until` |
| `_list_notifications` | `EXEC` | `since, until` |
