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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>action_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.action_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource Id. |
| `name` | `string` | The name of the resource. |
| `location` | `string` | The location of the resource. Since Azure Activity Log Alerts is a global service, the location of the rules should always be 'global'. |
| `properties` | `object` | A pointer to an Azure Action Group. |
| `tags` | `object` | The tags of the resource. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, tenantActionGroupName` | Get an action group. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Get a list of all action groups in a resource group. |
| `list_by_subscription_id` | `SELECT` | `subscriptionId` | Get a list of all action groups in a subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, tenantActionGroupName` | Create a new action group or update an existing one. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, tenantActionGroupName` | Delete an action group. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Get a list of all action groups in a resource group. |
| `_list_by_subscription_id` | `EXEC` | `subscriptionId` | Get a list of all action groups in a subscription. |
| `enable_receiver` | `EXEC` | `resourceGroupName, subscriptionId, tenantActionGroupName, data__receiverName` | Enable a receiver in an action group. This changes the receiver's status from Disabled to Enabled. This operation is only supported for Email or SMS receivers. |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, tenantActionGroupName` | Updates an existing action group's tags. To update other fields use the CreateOrUpdate method. |
