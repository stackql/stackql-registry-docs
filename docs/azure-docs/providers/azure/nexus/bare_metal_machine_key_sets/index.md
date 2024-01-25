---
title: bare_metal_machine_key_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - bare_metal_machine_key_sets
  - nexus
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
<tr><td><b>Name</b></td><td><code>bare_metal_machine_key_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.nexus.bare_metal_machine_key_sets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` |  |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` |  |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `bareMetalMachineKeySetName, clusterName, resourceGroupName, subscriptionId` | Get bare metal machine key set of the provided cluster. |
| `list_by_cluster` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Get a list of bare metal machine key sets for the provided cluster. |
| `create_or_update` | `INSERT` | `bareMetalMachineKeySetName, clusterName, resourceGroupName, subscriptionId, data__extendedLocation, data__properties` | Create a new bare metal machine key set or update the existing one for the provided cluster. |
| `delete` | `DELETE` | `bareMetalMachineKeySetName, clusterName, resourceGroupName, subscriptionId` | Delete the bare metal machine key set of the provided cluster. |
| `_list_by_cluster` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Get a list of bare metal machine key sets for the provided cluster. |
| `update` | `EXEC` | `bareMetalMachineKeySetName, clusterName, resourceGroupName, subscriptionId` | Patch properties of bare metal machine key set for the provided cluster, or update the tags associated with it. Properties and tag updates can be done independently. |
