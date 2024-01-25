---
title: restore_point_collections
hide_title: false
hide_table_of_contents: false
keywords:
  - restore_point_collections
  - compute
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
<tr><td><b>Name</b></td><td><code>restore_point_collections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.restore_point_collections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `location` | `string` | Resource location |
| `properties` | `object` | The restore point collection properties. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, restorePointCollectionName, subscriptionId` | The operation to get the restore point collection. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Gets the list of restore point collections in a resource group. |
| `create_or_update` | `INSERT` | `resourceGroupName, restorePointCollectionName, subscriptionId` | The operation to create or update the restore point collection. Please refer to https://aka.ms/RestorePoints for more details. When updating a restore point collection, only tags may be modified. |
| `delete` | `DELETE` | `resourceGroupName, restorePointCollectionName, subscriptionId` | The operation to delete the restore point collection. This operation will also delete all the contained restore points. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Gets the list of restore point collections in a resource group. |
| `update` | `EXEC` | `resourceGroupName, restorePointCollectionName, subscriptionId` | The operation to update the restore point collection. |
