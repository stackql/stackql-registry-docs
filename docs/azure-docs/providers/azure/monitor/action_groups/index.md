---
title: action_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - action_groups
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
<tr><td><b>Name</b></td><td><code>action_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.action_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource Id. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. Azure Activity Log Alert rules are supported on Global, West Europe and North Europe regions. |
| <CopyableCode code="properties" /> | `object` | A pointer to an Azure Action Group. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="actionGroupName, resourceGroupName, subscriptionId" /> | Get an action group. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a list of all action groups in a resource group. |
| <CopyableCode code="list_by_subscription_id" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a list of all action groups in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="actionGroupName, resourceGroupName, subscriptionId" /> | Create a new action group or update an existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="actionGroupName, resourceGroupName, subscriptionId" /> | Delete an action group. |
| <CopyableCode code="enable_receiver" /> | `EXEC` | <CopyableCode code="actionGroupName, resourceGroupName, subscriptionId, data__receiverName" /> | Enable a receiver in an action group. This changes the receiver's status from Disabled to Enabled. This operation is only supported for Email or SMS receivers. |
| <CopyableCode code="reconcile_nsp" /> | `EXEC` | <CopyableCode code="actionGroupName, networkSecurityPerimeterConfigurationName, resourceGroupName, subscriptionId" /> | Reconciles a specified NSP configuration for specified action group. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="actionGroupName, resourceGroupName, subscriptionId" /> | Updates an existing action group's tags. To update other fields use the CreateOrUpdate method. |
