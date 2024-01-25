---
title: cloud_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_endpoints
  - storage_sync
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
<tr><td><b>Name</b></td><td><code>cloud_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_sync.cloud_endpoints</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Get a given CloudEndpoint. |
| `list_by_sync_group` | `SELECT` | `resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Get a CloudEndpoint List. |
| `create` | `INSERT` | `cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Create a new CloudEndpoint. |
| `delete` | `DELETE` | `cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Delete a given CloudEndpoint. |
| `_list_by_sync_group` | `EXEC` | `resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Get a CloudEndpoint List. |
| `afs_share_metadata_certificate_public_keys` | `EXEC` | `cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Get the AFS file share metadata signing certificate public keys. |
| `post_backup` | `EXEC` | `cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Post Backup a given CloudEndpoint. |
| `post_restore` | `EXEC` | `cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Post Restore a given CloudEndpoint. |
| `pre_backup` | `EXEC` | `cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Pre Backup a given CloudEndpoint. |
| `pre_restore` | `EXEC` | `cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Pre Restore a given CloudEndpoint. |
| `restoreheartbeat` | `EXEC` | `cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Restore Heartbeat a given CloudEndpoint. |
| `trigger_change_detection` | `EXEC` | `cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Triggers detection of changes performed on Azure File share connected to the specified Azure File Sync Cloud Endpoint. |
