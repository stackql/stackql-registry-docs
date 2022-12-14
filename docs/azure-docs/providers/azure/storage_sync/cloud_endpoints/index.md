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
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `CloudEndpoints_Get` | `SELECT` | `cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Get a given CloudEndpoint. |
| `CloudEndpoints_ListBySyncGroup` | `SELECT` | `resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Get a CloudEndpoint List. |
| `CloudEndpoints_Create` | `INSERT` | `cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Create a new CloudEndpoint. |
| `CloudEndpoints_Delete` | `DELETE` | `cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Delete a given CloudEndpoint. |
| `CloudEndpoints_AfsShareMetadataCertificatePublicKeys` | `EXEC` | `cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Get the AFS file share metadata signing certificate public keys. |
| `CloudEndpoints_PostBackup` | `EXEC` | `cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Post Backup a given CloudEndpoint. |
| `CloudEndpoints_PostRestore` | `EXEC` | `cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Post Restore a given CloudEndpoint. |
| `CloudEndpoints_PreBackup` | `EXEC` | `cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Pre Backup a given CloudEndpoint. |
| `CloudEndpoints_PreRestore` | `EXEC` | `cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Pre Restore a given CloudEndpoint. |
| `CloudEndpoints_TriggerChangeDetection` | `EXEC` | `cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Triggers detection of changes performed on Azure File share connected to the specified Azure File Sync Cloud Endpoint. |
| `CloudEndpoints_restoreheartbeat` | `EXEC` | `cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName` | Restore Heartbeat a given CloudEndpoint. |
