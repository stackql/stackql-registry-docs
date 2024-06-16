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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.volumes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Volume properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="zones" /> | `array` | Availability Zone |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Get the details of the specified volume |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId" /> | List all volumes within the capacity pool |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName, data__location, data__properties" /> | Create or update the specified volume within the capacity pool |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Delete the specified volume |
| <CopyableCode code="authorize_replication" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Authorize the replication connection on the source volume |
| <CopyableCode code="break_file_locks" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Break all the file locks on a volume |
| <CopyableCode code="break_replication" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Break the replication connection on the destination volume |
| <CopyableCode code="finalize_on_prem_migration" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Finalizes the migration of a volume by performing a final sync on the replication, breaking and releasing the replication, and breaking the cluster peering if no other migration is active. |
| <CopyableCode code="finalize_relocation" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Finalizes the relocation of the volume and cleans up the old volume. |
| <CopyableCode code="peer_cluster_for_on_prem_migration" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName, data__peerAddresses" /> | Starts peering the cluster for this migration volume |
| <CopyableCode code="perform_replication_transfer" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Performs an adhoc replication transfer on a volume with volumeType Migration |
| <CopyableCode code="pool_change" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName, data__newPoolResourceId" /> | Moves volume to another pool |
| <CopyableCode code="populate_availability_zone" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | This operation will populate availability zone information for a volume |
| <CopyableCode code="re_initialize_replication" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Re-Initializes the replication connection on the destination volume |
| <CopyableCode code="reestablish_replication" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Re-establish a previously deleted replication between 2 volumes that have a common ad-hoc or policy-based snapshots |
| <CopyableCode code="relocate" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Relocates volume to a new stamp |
| <CopyableCode code="replication_status" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Get the status of the replication |
| <CopyableCode code="reset_cifs_password" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Reset cifs password from volume |
| <CopyableCode code="resync_replication" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Resync the connection on the destination volume. If the operation is ran on the source volume it will reverse-resync the connection and sync from destination to source. |
| <CopyableCode code="revert" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Revert a volume to the snapshot specified in the body |
| <CopyableCode code="revert_relocation" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Reverts the volume relocation process, cleans up the new volume and starts using the former-existing volume. |
| <CopyableCode code="split_clone_from_parent" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> |  Split operation to convert clone volume to an independent volume. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Patch the specified volume |
