---
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
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
<tr><td><b>Name</b></td><td><code>snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.snapshots</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
| `properties` | `object` | Snapshot resource properties. |
| `location` | `string` | Resource location |
| `managedBy` | `string` | Unused. Always Null. |
| `sku` | `object` | The snapshots sku name. Can be Standard_LRS, Premium_LRS, or Standard_ZRS. This is an optional parameter for incremental snapshot and the default behavior is the SKU will be set to the same sku as the previous snapshot |
| `extendedLocation` | `object` | The complex type of the extended location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Snapshots_Get` | `SELECT` | `resourceGroupName, snapshotName, subscriptionId` | Gets information about a snapshot. |
| `Snapshots_List` | `SELECT` | `subscriptionId` | Lists snapshots under a subscription. |
| `Snapshots_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists snapshots under a resource group. |
| `Snapshots_CreateOrUpdate` | `INSERT` | `resourceGroupName, snapshotName, subscriptionId` | Creates or updates a snapshot. |
| `Snapshots_Delete` | `DELETE` | `resourceGroupName, snapshotName, subscriptionId` | Deletes a snapshot. |
| `Snapshots_GrantAccess` | `EXEC` | `resourceGroupName, snapshotName, subscriptionId, data__access, data__durationInSeconds` | Grants access to a snapshot. |
| `Snapshots_RevokeAccess` | `EXEC` | `resourceGroupName, snapshotName, subscriptionId` | Revokes access to a snapshot. |
| `Snapshots_Update` | `EXEC` | `resourceGroupName, snapshotName, subscriptionId` | Updates (patches) a snapshot. |
