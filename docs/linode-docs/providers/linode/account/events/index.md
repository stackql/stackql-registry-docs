---
title: events
hide_title: false
hide_table_of_contents: false
keywords:
  - events
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
<tr><td><b>Name</b></td><td><code>events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.account.events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The unique ID of this Event. |
| `username` | `string` | The username of the User who caused the Event.<br /> |
| `entity` | `object` | Detailed information about the Event's entity, including ID, type, label, and URL used to access it.<br /> |
| `status` | `string` | The current status of this Event. |
| `secondary_entity` | `object` | Detailed information about the Event's secondary entity, which provides additional information<br />for events such as, but not limited to, `linode_boot`, `linode_reboot`, `linode_create`, and `linode_clone` Event actions.<br /> |
| `time_remaining` | `string` | The estimated time remaining until the completion of this Event. This value is only returned for some in-progress migration events. For all other in-progress events, the `percent_complete` attribute will indicate about how much more work is to be done.<br /> |
| `message` | `string` | Provides additional information about the event. Additional information may include, but is not limited to, a more detailed representation of events which can help diagnose non-obvious failures.<br /> |
| `created` | `string` | When this Event was created. |
| `action` | `string` | The action that caused this Event. New actions may be added in the future.<br /> |
| `read` | `boolean` | If this Event has been read. |
| `percent_complete` | `integer` | A percentage estimating the amount of time remaining for an Event.<br />Returns `null` for notification events.<br /> |
| `duration` | `number` | The total duration in seconds that it takes for the Event to complete.<br /> |
| `rate` | `string` | The rate of completion of the Event. Only some Events will return rate; for example, migration and resize Events.<br /> |
| `seen` | `boolean` | If this Event has been seen. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getEvent` | `SELECT` | `eventId` | Returns a single Event object.<br /> |
| `getEvents` | `SELECT` |  | Returns a collection of Event objects representing actions taken on your Account from the last 90 days. The Events returned depend on your grants.<br /> |
| `_getEvent` | `EXEC` | `eventId` | Returns a single Event object.<br /> |
| `_getEvents` | `EXEC` |  | Returns a collection of Event objects representing actions taken on your Account from the last 90 days. The Events returned depend on your grants.<br /> |
| `eventRead` | `EXEC` | `eventId` | Marks a single Event as read. |
| `eventSeen` | `EXEC` | `eventId` | Marks all Events up to and including this Event by ID as seen.<br /> |
