---
title: activity_log_alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - activity_log_alerts
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
<tr><td><b>Name</b></td><td><code>activity_log_alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.activity_log_alerts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource Id. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. Azure Activity Log Alert rules are supported on Global, West Europe and North Europe regions. |
| <CopyableCode code="properties" /> | `object` | An Azure Activity Log Alert rule. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="activityLogAlertName, resourceGroupName, subscriptionId" /> | Get an Activity Log Alert rule. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a list of all Activity Log Alert rules in a resource group. |
| <CopyableCode code="list_by_subscription_id" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a list of all Activity Log Alert rules in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="activityLogAlertName, resourceGroupName, subscriptionId" /> | Create a new Activity Log Alert rule or update an existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="activityLogAlertName, resourceGroupName, subscriptionId" /> | Delete an Activity Log Alert rule. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="activityLogAlertName, resourceGroupName, subscriptionId" /> | Updates 'tags' and 'enabled' fields in an existing Alert rule. This method is used to update the Alert rule tags, and to enable or disable the Alert rule. To update other fields use CreateOrUpdate operation. |
