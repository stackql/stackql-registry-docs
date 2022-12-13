---
title: replication_protectable_items
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_protectable_items
  - recovery_services_site_recovery
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
<tr><td><b>Name</b></td><td><code>replication_protectable_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_site_recovery.replication_protectable_items</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `properties` | `object` | Replication protected item custom data details. |
| `type` | `string` | Resource Type |
| `location` | `string` | Resource Location |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ReplicationProtectableItems_Get` | `SELECT` | `api-version, fabricName, protectableItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId` | The operation to get the details of a protectable item. |
| `ReplicationProtectableItems_ListByReplicationProtectionContainers` | `SELECT` | `api-version, fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId` | Lists the protectable items in a protection container. |
