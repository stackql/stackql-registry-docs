---
title: restore_points
hide_title: false
hide_table_of_contents: false
keywords:
  - restore_points
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
<tr><td><b>Name</b></td><td><code>restore_points</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.restore_points</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `type` | `string` | Resource type |
| `properties` | `object` | The restore point properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RestorePoints_Get` | `SELECT` | `resourceGroupName, restorePointCollectionName, restorePointName, subscriptionId` | The operation to get the restore point. |
| `RestorePoints_Create` | `INSERT` | `resourceGroupName, restorePointCollectionName, restorePointName, subscriptionId` | The operation to create the restore point. Updating properties of an existing restore point is not allowed |
| `RestorePoints_Delete` | `DELETE` | `resourceGroupName, restorePointCollectionName, restorePointName, subscriptionId` | The operation to delete the restore point. |
