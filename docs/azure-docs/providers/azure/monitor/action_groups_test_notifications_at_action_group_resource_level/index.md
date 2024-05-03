---
title: action_groups_test_notifications_at_action_group_resource_level
hide_title: false
hide_table_of_contents: false
keywords:
  - action_groups_test_notifications_at_action_group_resource_level
  - monitor
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>action_groups_test_notifications_at_action_group_resource_level</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.action_groups_test_notifications_at_action_group_resource_level" /></td></tr>
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
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="notificationId, resourceGroupName, subscriptionId, tenantActionGroupName" /> |
