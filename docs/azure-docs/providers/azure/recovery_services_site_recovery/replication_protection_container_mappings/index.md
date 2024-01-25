---
title: replication_protection_container_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_protection_container_mappings
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
<tr><td><b>Name</b></td><td><code>replication_protection_container_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_site_recovery.replication_protection_container_mappings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `location` | `string` | Resource Location |
| `properties` | `object` | Protection container mapping properties. |
| `type` | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, fabricName, mappingName, protectionContainerName, resourceGroupName, resourceName, subscriptionId` | Gets the details of a protection container mapping. |
| `list` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Lists the protection container mappings in the vault. |
| `list_by_replication_protection_containers` | `SELECT` | `api-version, fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId` | Lists the protection container mappings for a protection container. |
| `create` | `INSERT` | `api-version, fabricName, mappingName, protectionContainerName, resourceGroupName, resourceName, subscriptionId` | The operation to create a protection container mapping. |
| `delete` | `DELETE` | `api-version, fabricName, mappingName, protectionContainerName, resourceGroupName, resourceName, subscriptionId` | The operation to delete or remove a protection container mapping. |
| `_list` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId` | Lists the protection container mappings in the vault. |
| `_list_by_replication_protection_containers` | `EXEC` | `api-version, fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId` | Lists the protection container mappings for a protection container. |
| `purge` | `EXEC` | `api-version, fabricName, mappingName, protectionContainerName, resourceGroupName, resourceName, subscriptionId` | The operation to purge(force delete) a protection container mapping. |
| `update` | `EXEC` | `api-version, fabricName, mappingName, protectionContainerName, resourceGroupName, resourceName, subscriptionId` | The operation to update protection container mapping. |
