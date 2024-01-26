---
title: volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes
  - netapp
  - azure_isv    
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
<tr><td><b>Id</b></td><td><code>azure_isv.netapp.volumes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Volume properties |
| `tags` | `object` | Resource tags. |
| `zones` | `array` | Availability Zone |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Get the details of the specified volume |
| `list` | `SELECT` | `accountName, poolName, resourceGroupName, subscriptionId` | List all volumes within the capacity pool |
| `create_or_update` | `INSERT` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName, data__location, data__properties` | Create or update the specified volume within the capacity pool |
| `delete` | `DELETE` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Delete the specified volume |
| `_list` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId` | List all volumes within the capacity pool |
| `authorize_replication` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Authorize the replication connection on the source volume |
| `break_file_locks` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Break all the file locks on a volume |
| `break_replication` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Break the replication connection on the destination volume |
| `finalize_relocation` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Finalizes the relocation of the volume and cleans up the old volume. |
| `pool_change` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName, data__newPoolResourceId` | Moves volume to another pool |
| `populate_availability_zone` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | This operation will populate availability zone information for a volume |
| `re_initialize_replication` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Re-Initializes the replication connection on the destination volume |
| `reestablish_replication` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Re-establish a previously deleted replication between 2 volumes that have a common ad-hoc or policy-based snapshots |
| `relocate` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Relocates volume to a new stamp |
| `replication_status` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Get the status of the replication |
| `reset_cifs_password` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Reset cifs password from volume |
| `resync_replication` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Resync the connection on the destination volume. If the operation is ran on the source volume it will reverse-resync the connection and sync from destination to source. |
| `revert` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Revert a volume to the snapshot specified in the body |
| `revert_relocation` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Reverts the volume relocation process, cleans up the new volume and starts using the former-existing volume. |
| `update` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Patch the specified volume |
