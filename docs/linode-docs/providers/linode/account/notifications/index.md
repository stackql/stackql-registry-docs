---
title: notifications
hide_title: false
hide_table_of_contents: false
keywords:
  - notifications
  - account
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notifications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.account.notifications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `until` | `string` | If this Notification has a duration, this will be the ending time for the Event/action. For example, if there is scheduled maintenance for one of our systems, `until` would be set to the end of the maintenance window.<br /> |
| `when` | `string` | If this Notification is of an Event that will happen at a fixed, future time, this is when the named action will be taken. For example, if a Linode is to be migrated in response to a Security Advisory, this field will contain the approximate time the Linode will be taken offline for migration.<br /> |
| `body` | `string` | A full description of this Notification, in markdown format.  Not all Notifications include bodies.<br /> |
| `entity` | `object` | Detailed information about the Notification. |
| `label` | `string` | A short description of this Notification.<br /> |
| `message` | `string` | A human-readable description of the Notification. |
| `severity` | `string` | The severity of this Notification.  This field can be used to decide how prominently to display the Notification, what color to make the display text, etc.<br /> |
| `type` | `string` | The type of Notification this is. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getNotifications` | `SELECT` |  |
| `_getNotifications` | `EXEC` |  |
