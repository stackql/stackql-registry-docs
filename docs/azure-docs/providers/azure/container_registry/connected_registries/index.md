---
title: connected_registries
hide_title: false
hide_table_of_contents: false
keywords:
  - connected_registries
  - container_registry
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
<tr><td><b>Name</b></td><td><code>connected_registries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry.connected_registries</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `connectedRegistryName, registryName, resourceGroupName, subscriptionId` | Gets the properties of the connected registry. |
| `list` | `SELECT` | `registryName, resourceGroupName, subscriptionId` | Lists all connected registries for the specified container registry. |
| `create` | `INSERT` | `connectedRegistryName, registryName, resourceGroupName, subscriptionId` | Creates a connected registry for a container registry with the specified parameters. |
| `delete` | `DELETE` | `connectedRegistryName, registryName, resourceGroupName, subscriptionId` | Deletes a connected registry from a container registry. |
| `_list` | `EXEC` | `registryName, resourceGroupName, subscriptionId` | Lists all connected registries for the specified container registry. |
| `deactivate` | `EXEC` | `connectedRegistryName, registryName, resourceGroupName, subscriptionId` | Deactivates the connected registry instance. |
| `update` | `EXEC` | `connectedRegistryName, registryName, resourceGroupName, subscriptionId` | Updates a connected registry with the specified parameters. |
