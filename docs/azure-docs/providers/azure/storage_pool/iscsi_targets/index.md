---
title: iscsi_targets
hide_title: false
hide_table_of_contents: false
keywords:
  - iscsi_targets
  - storage_pool
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
<tr><td><b>Name</b></td><td><code>iscsi_targets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_pool.iscsi_targets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `managedBy` | `string` | Azure resource id. Indicates if this resource is managed by another Azure resource. |
| `managedByExtended` | `array` | List of Azure resource ids that manage this resource. |
| `properties` | `object` | Response properties for iSCSI Target operations. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IscsiTargets_Get` | `SELECT` | `diskPoolName, iscsiTargetName, resourceGroupName, subscriptionId` | Get an iSCSI Target. |
| `IscsiTargets_ListByDiskPool` | `SELECT` | `diskPoolName, resourceGroupName, subscriptionId` | Get iSCSI Targets in a Disk pool. |
| `IscsiTargets_CreateOrUpdate` | `INSERT` | `diskPoolName, iscsiTargetName, resourceGroupName, subscriptionId, data__properties` | Create or Update an iSCSI Target. |
| `IscsiTargets_Delete` | `DELETE` | `diskPoolName, iscsiTargetName, resourceGroupName, subscriptionId` | Delete an iSCSI Target. |
| `IscsiTargets_Update` | `EXEC` | `diskPoolName, iscsiTargetName, resourceGroupName, subscriptionId, data__properties` | Update an iSCSI Target. |
