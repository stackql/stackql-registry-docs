---
title: managed_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instances
  - sql
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
<tr><td><b>Name</b></td><td><code>managed_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Azure Active Directory identity configuration for a resource. |
| `location` | `string` | Resource location. |
| `properties` | `object` | The properties of a managed instance. |
| `sku` | `object` | An ARM Resource SKU. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `subscriptionId` | Gets a list of all managed instances in the subscription. |
| `list_by_instance_pool` | `SELECT` | `instancePoolName, resourceGroupName, subscriptionId` | Gets a list of all managed instances in an instance pool. |
| `list_by_managed_instance` | `SELECT` | `managedInstanceName, resourceGroupName, subscriptionId` | Get top resource consuming queries of a managed instance. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of managed instances in a resource group. |
| `create_or_update` | `INSERT` | `managedInstanceName, resourceGroupName, subscriptionId, data__location` | Creates or updates a managed instance. |
| `delete` | `DELETE` | `managedInstanceName, resourceGroupName, subscriptionId` | Deletes a managed instance. |
| `_list` | `EXEC` | `subscriptionId` | Gets a list of all managed instances in the subscription. |
| `_list_by_instance_pool` | `EXEC` | `instancePoolName, resourceGroupName, subscriptionId` | Gets a list of all managed instances in an instance pool. |
| `_list_by_managed_instance` | `EXEC` | `managedInstanceName, resourceGroupName, subscriptionId` | Get top resource consuming queries of a managed instance. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets a list of managed instances in a resource group. |
| `exec_get` | `EXEC` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets a managed instance. |
| `failover` | `EXEC` | `managedInstanceName, resourceGroupName, subscriptionId` | Failovers a managed instance. |
| `refresh_status` | `EXEC` | `managedInstanceName, resourceGroupName, subscriptionId` | Refresh external governance enablement status. |
| `start` | `EXEC` | `managedInstanceName, resourceGroupName, subscriptionId` | Starts the managed instance. |
| `stop` | `EXEC` | `managedInstanceName, resourceGroupName, subscriptionId` | Stops the managed instance. |
| `update` | `EXEC` | `managedInstanceName, resourceGroupName, subscriptionId` | Updates a managed instance. |
