---
title: notifications
hide_title: false
hide_table_of_contents: false
keywords:
  - notifications
  - advisorynotifications
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notifications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="advisorynotifications.notifications" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the notification. Format: organizations/&#123;organization&#125;/locations/&#123;location&#125;/notifications/&#123;notification&#125; or projects/&#123;project&#125;/locations/&#123;location&#125;/notifications/&#123;notification&#125;. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time the notification was created. |
| <CopyableCode code="messages" /> | `array` | A list of messages in the notification. |
| <CopyableCode code="notificationType" /> | `string` | Type of notification |
| <CopyableCode code="subject" /> | `object` | A subject line of a notification. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, notificationsId, organizationsId" /> | Gets a notification. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists notifications under a given parent. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, organizationsId" /> | Lists notifications under a given parent. |
