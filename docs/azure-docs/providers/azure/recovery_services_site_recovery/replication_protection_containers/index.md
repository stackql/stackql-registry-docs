---
title: replication_protection_containers
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_protection_containers
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
<tr><td><b>Name</b></td><td><code>replication_protection_containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_site_recovery.replication_protection_containers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `location` | `string` | Resource Location |
| `properties` | `object` | Protection profile custom data details. |
| `type` | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId` | Gets the details of a protection container. |
| `list` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Lists the protection containers in a vault. |
| `list_by_replication_fabrics` | `SELECT` | `api-version, fabricName, resourceGroupName, resourceName, subscriptionId` | Lists the protection containers in the specified fabric. |
| `create` | `INSERT` | `api-version, fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId` | Operation to create a protection container. |
| `delete` | `DELETE` | `api-version, fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId` | Operation to remove a protection container. |
| `_list` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId` | Lists the protection containers in a vault. |
| `_list_by_replication_fabrics` | `EXEC` | `api-version, fabricName, resourceGroupName, resourceName, subscriptionId` | Lists the protection containers in the specified fabric. |
| `discover_protectable_item` | `EXEC` | `api-version, fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId` | The operation to a add a protectable item to a protection container(Add physical server). |
| `switch_protection` | `EXEC` | `api-version, fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId` | Operation to switch protection from one container to another or one replication provider to another. |
