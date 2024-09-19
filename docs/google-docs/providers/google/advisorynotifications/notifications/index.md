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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>notifications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notifications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.advisorynotifications.notifications" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the notification. Format: organizations/{organization}/locations/{location}/notifications/{notification} or projects/{project}/locations/{location}/notifications/{notification}. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time the notification was created. |
| <CopyableCode code="messages" /> | `array` | A list of messages in the notification. |
| <CopyableCode code="notificationType" /> | `string` | Type of notification |
| <CopyableCode code="subject" /> | `object` | A subject line of a notification. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, notificationsId, projectsId" /> | Gets a notification. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists notifications under a given parent. |

## `SELECT` examples

Lists notifications under a given parent.

```sql
SELECT
name,
createTime,
messages,
notificationType,
subject
FROM google.advisorynotifications.notifications
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
