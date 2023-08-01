---
title: instance_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_pools
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
<tr><td><b>Name</b></td><td><code>instance_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.instance_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | Resource location. |
| `properties` | `object` | Properties of an instance pool. |
| `sku` | `object` | An ARM Resource SKU. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `InstancePools_Get` | `SELECT` | `instancePoolName, resourceGroupName, subscriptionId` | Gets an instance pool. |
| `InstancePools_List` | `SELECT` | `subscriptionId` | Gets a list of all instance pools in the subscription. |
| `InstancePools_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of instance pools in the resource group |
| `InstancePools_CreateOrUpdate` | `INSERT` | `instancePoolName, resourceGroupName, subscriptionId, data__location` | Creates or updates an instance pool. |
| `InstancePools_Delete` | `DELETE` | `instancePoolName, resourceGroupName, subscriptionId` | Deletes an instance pool |
| `InstancePools_Update` | `EXEC` | `instancePoolName, resourceGroupName, subscriptionId` | Updates an instance pool. |
