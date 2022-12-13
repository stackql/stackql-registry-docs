---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_sync.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Storage Sync Service Properties object. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `StorageSyncServices_Get` | `SELECT` | `resourceGroupName, storageSyncServiceName, subscriptionId` | Get a given StorageSyncService. |
| `StorageSyncServices_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Get a StorageSyncService list by Resource group name. |
| `StorageSyncServices_ListBySubscription` | `SELECT` | `subscriptionId` | Get a StorageSyncService list by subscription. |
| `StorageSyncServices_Create` | `INSERT` | `resourceGroupName, storageSyncServiceName, subscriptionId, data__location` | Create a new StorageSyncService. |
| `StorageSyncServices_Delete` | `DELETE` | `resourceGroupName, storageSyncServiceName, subscriptionId` | Delete a given StorageSyncService. |
| `StorageSyncServices_CheckNameAvailability` | `EXEC` | `locationName, subscriptionId, data__name, data__type` | Check the give namespace name availability. |
| `StorageSyncServices_Update` | `EXEC` | `resourceGroupName, storageSyncServiceName, subscriptionId` | Patch a given StorageSyncService. |
