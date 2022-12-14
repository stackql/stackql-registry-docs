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
| `properties` | `object` | Network Mapping Properties. |
| `type` | `string` | Resource Type |
| `location` | `string` | Resource Location |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ReplicationNetworkMappings_Get` | `SELECT` | `api-version, fabricName, networkMappingName, networkName, resourceGroupName, resourceName, subscriptionId` | Gets the details of an ASR network mapping. |
| `ReplicationNetworkMappings_List` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Lists all ASR network mappings in the vault. |
| `ReplicationNetworkMappings_ListByReplicationNetworks` | `SELECT` | `api-version, fabricName, networkName, resourceGroupName, resourceName, subscriptionId` | Lists all ASR network mappings for the specified network. |
| `ReplicationNetworkMappings_Create` | `INSERT` | `api-version, fabricName, networkMappingName, networkName, resourceGroupName, resourceName, subscriptionId, data__properties` | The operation to create an ASR network mapping. |
| `ReplicationNetworkMappings_Delete` | `DELETE` | `api-version, fabricName, networkMappingName, networkName, resourceGroupName, resourceName, subscriptionId` | The operation to delete a network mapping. |
| `ReplicationNetworkMappings_Update` | `EXEC` | `api-version, fabricName, networkMappingName, networkName, resourceGroupName, resourceName, subscriptionId` | The operation to update an ASR network mapping. |
