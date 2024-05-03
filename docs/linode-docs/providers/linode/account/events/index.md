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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.account.events" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | The unique ID of this Event. |
| <CopyableCode code="action" /> | `string` | The action that caused this Event. New actions may be added in the future.<br /> |
| <CopyableCode code="created" /> | `string` | When this Event was created. |
| <CopyableCode code="duration" /> | `number` | The total duration in seconds that it takes for the Event to complete.<br /> |
| <CopyableCode code="entity" /> | `object` | Detailed information about the Event's entity, including ID, type, label, and URL used to access it.<br /> |
| <CopyableCode code="message" /> | `string` | Provides additional information about the event. Additional information may include, but is not limited to, a more detailed representation of events which can help diagnose non-obvious failures.<br /> |
| <CopyableCode code="percent_complete" /> | `integer` | A percentage estimating the amount of time remaining for an Event.<br />Returns `null` for notification events.<br /> |
| <CopyableCode code="rate" /> | `string` | The rate of completion of the Event. Only some Events will return rate; for example, migration and resize Events.<br /> |
| <CopyableCode code="read" /> | `boolean` | If this Event has been read. |
| <CopyableCode code="secondary_entity" /> | `object` | Detailed information about the Event's secondary entity, which provides additional information<br />for events such as, but not limited to, `linode_boot`, `linode_reboot`, `linode_create`, and `linode_clone` Event actions.<br /> |
| <CopyableCode code="seen" /> | `boolean` | If this Event has been seen. |
| <CopyableCode code="status" /> | `string` | The current status of this Event. |
| <CopyableCode code="time_remaining" /> | `string` | The estimated time remaining until the completion of this Event. This value is only returned for some in-progress migration events. For all other in-progress events, the `percent_complete` attribute will indicate about how much more work is to be done.<br /> |
| <CopyableCode code="username" /> | `string` | The username of the User who caused the Event.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getEvent" /> | `SELECT` | <CopyableCode code="eventId" /> | Returns a single Event object.<br /> |
| <CopyableCode code="getEvents" /> | `SELECT` |  | Returns a collection of Event objects representing actions taken on your Account from the last 90 days. The Events returned depend on your grants.<br /> |
| <CopyableCode code="_getEvent" /> | `EXEC` | <CopyableCode code="eventId" /> | Returns a single Event object.<br /> |
| <CopyableCode code="_getEvents" /> | `EXEC` |  | Returns a collection of Event objects representing actions taken on your Account from the last 90 days. The Events returned depend on your grants.<br /> |
| <CopyableCode code="eventRead" /> | `EXEC` | <CopyableCode code="eventId" /> | Marks a single Event as read. |
| <CopyableCode code="eventSeen" /> | `EXEC` | <CopyableCode code="eventId" /> | Marks all Events up to and including this Event by ID as seen.<br /> |
