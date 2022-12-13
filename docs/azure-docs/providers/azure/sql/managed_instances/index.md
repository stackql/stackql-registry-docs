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
| `tags` | `object` | Resource tags. |
| `identity` | `object` | Azure Active Directory identity configuration for a resource. |
| `location` | `string` | Resource location. |
| `properties` | `object` | The properties of a managed instance. |
| `sku` | `object` | An ARM Resource SKU. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedInstances_List` | `SELECT` | `subscriptionId` | Gets a list of all managed instances in the subscription. |
| `ManagedInstances_ListByInstancePool` | `SELECT` | `instancePoolName, resourceGroupName, subscriptionId` | Gets a list of all managed instances in an instance pool. |
| `ManagedInstances_ListByManagedInstance` | `SELECT` | `managedInstanceName, resourceGroupName, subscriptionId` | Get top resource consuming queries of a managed instance. |
| `ManagedInstances_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of managed instances in a resource group. |
| `ManagedInstances_CreateOrUpdate` | `INSERT` | `managedInstanceName, resourceGroupName, subscriptionId, data__location` | Creates or updates a managed instance. |
| `ManagedInstances_Delete` | `DELETE` | `managedInstanceName, resourceGroupName, subscriptionId` | Deletes a managed instance. |
| `ManagedInstances_Failover` | `EXEC` | `managedInstanceName, resourceGroupName, subscriptionId` | Failovers a managed instance. |
| `ManagedInstances_Get` | `EXEC` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets a managed instance. |
| `ManagedInstances_Update` | `EXEC` | `managedInstanceName, resourceGroupName, subscriptionId` | Updates a managed instance. |
