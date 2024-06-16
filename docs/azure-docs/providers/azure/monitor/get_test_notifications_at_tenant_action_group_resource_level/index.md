---
title: get_test_notifications_at_tenant_action_group_resource_level
hide_title: false
hide_table_of_contents: false
keywords:
  - get_test_notifications_at_tenant_action_group_resource_level
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
<tr><td><b>Name</b></td><td><code>get_test_notifications_at_tenant_action_group_resource_level</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.get_test_notifications_at_tenant_action_group_resource_level" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_test_notifications_at_tenant_action_group_resource_level" /> | `EXEC` | <CopyableCode code="actionGroupName, managementGroupId, notificationId, tenantId" /> |
