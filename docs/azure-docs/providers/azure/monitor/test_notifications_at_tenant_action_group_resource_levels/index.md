---
title: test_notifications_at_tenant_action_group_resource_levels
hide_title: false
hide_table_of_contents: false
keywords:
  - test_notifications_at_tenant_action_group_resource_levels
  - monitor
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

Creates, updates, deletes, gets or lists a <code>test_notifications_at_tenant_action_group_resource_levels</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>test_notifications_at_tenant_action_group_resource_levels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.test_notifications_at_tenant_action_group_resource_levels" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="actionDetails" /> | `array` | The list of action detail |
| <CopyableCode code="completedTime" /> | `string` | The completed time |
| <CopyableCode code="context" /> | `object` | The context info |
| <CopyableCode code="createdTime" /> | `string` | The created time |
| <CopyableCode code="state" /> | `string` | The overall state |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="actionGroupName, managementGroupId, notificationId, tenantId" /> | Get the test notifications by the notification id |

## `SELECT` examples

Get the test notifications by the notification id


```sql
SELECT
actionDetails,
completedTime,
context,
createdTime,
state
FROM azure.monitor.test_notifications_at_tenant_action_group_resource_levels
WHERE actionGroupName = '{{ actionGroupName }}'
AND managementGroupId = '{{ managementGroupId }}'
AND notificationId = '{{ notificationId }}'
AND tenantId = '{{ tenantId }}';
```