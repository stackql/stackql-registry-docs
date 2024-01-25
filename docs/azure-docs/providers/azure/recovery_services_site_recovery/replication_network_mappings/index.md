---
title: replication_network_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_network_mappings
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
<tr><td><b>Name</b></td><td><code>replication_network_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_site_recovery.replication_network_mappings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `location` | `string` | Resource Location |
| `properties` | `object` | Network Mapping Properties. |
| `type` | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, fabricName, networkMappingName, networkName, resourceGroupName, resourceName, subscriptionId` | Gets the details of an ASR network mapping. |
| `list` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Lists all ASR network mappings in the vault. |
| `list_by_replication_networks` | `SELECT` | `api-version, fabricName, networkName, resourceGroupName, resourceName, subscriptionId` | Lists all ASR network mappings for the specified network. |
| `create` | `INSERT` | `api-version, fabricName, networkMappingName, networkName, resourceGroupName, resourceName, subscriptionId, data__properties` | The operation to create an ASR network mapping. |
| `delete` | `DELETE` | `api-version, fabricName, networkMappingName, networkName, resourceGroupName, resourceName, subscriptionId` | The operation to delete a network mapping. |
| `_list` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId` | Lists all ASR network mappings in the vault. |
| `_list_by_replication_networks` | `EXEC` | `api-version, fabricName, networkName, resourceGroupName, resourceName, subscriptionId` | Lists all ASR network mappings for the specified network. |
| `update` | `EXEC` | `api-version, fabricName, networkMappingName, networkName, resourceGroupName, resourceName, subscriptionId` | The operation to update an ASR network mapping. |
