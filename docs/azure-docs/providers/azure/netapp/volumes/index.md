---
title: volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes
  - netapp
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
<tr><td><b>Name</b></td><td><code>volumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.netapp.volumes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `zones` | `array` | Availability Zone |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Volume properties |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Volumes_Get` | `SELECT` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Get the details of the specified volume |
| `Volumes_List` | `SELECT` | `accountName, poolName, resourceGroupName, subscriptionId` | List all volumes within the capacity pool |
| `Volumes_CreateOrUpdate` | `INSERT` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName, data__location, data__properties` | Create or update the specified volume within the capacity pool |
| `Volumes_Delete` | `DELETE` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Delete the specified volume |
| `Volumes_AuthorizeReplication` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Authorize the replication connection on the source volume |
| `Volumes_BreakReplication` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Break the replication connection on the destination volume |
| `Volumes_DeleteReplication` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Delete the replication connection on the destination volume, and send release to the source replication |
| `Volumes_FinalizeRelocation` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Finalizes the relocation of the volume and cleans up the old volume. |
| `Volumes_ListReplications` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | List all replications for a specified volume |
| `Volumes_PoolChange` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName, data__newPoolResourceId` | Moves volume to another pool |
| `Volumes_ReInitializeReplication` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Re-Initializes the replication connection on the destination volume |
| `Volumes_ReestablishReplication` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Re-establish a previously deleted replication between 2 volumes that have a common ad-hoc or policy-based snapshots |
| `Volumes_Relocate` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Relocates volume to a new stamp |
| `Volumes_ReplicationStatus` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Get the status of the replication |
| `Volumes_ResetCifsPassword` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Reset cifs password from volume |
| `Volumes_ResyncReplication` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Resync the connection on the destination volume. If the operation is ran on the source volume it will reverse-resync the connection and sync from destination to source. |
| `Volumes_Revert` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Revert a volume to the snapshot specified in the body |
| `Volumes_RevertRelocation` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Reverts the volume relocation process, cleans up the new volume and starts using the former-existing volume. |
| `Volumes_Update` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Patch the specified volume |
