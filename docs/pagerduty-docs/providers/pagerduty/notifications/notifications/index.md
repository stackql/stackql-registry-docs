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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notifications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.notifications.notifications" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="" /> | `string` |  |
| <CopyableCode code="address" /> | `string` | The address where the notification was sent. This will be null for notification type `push_notification`. |
| <CopyableCode code="conferenceAddress" /> | `string` | The address of the conference bridge |
| <CopyableCode code="started_at" /> | `string` | The time at which the notification was sent |
| <CopyableCode code="status" /> | `string` |  |
| <CopyableCode code="type" /> | `string` | The type of notification. |
| <CopyableCode code="user" /> | `object` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_notifications" /> | `SELECT` | <CopyableCode code="since, until" /> |
| <CopyableCode code="_list_notifications" /> | `EXEC` | <CopyableCode code="since, until" /> |
