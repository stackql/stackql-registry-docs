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
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `properties` | `object` | The properties of a connected registry. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ConnectedRegistries_Get` | `SELECT` | `connectedRegistryName, registryName, resourceGroupName, subscriptionId` | Gets the properties of the connected registry. |
| `ConnectedRegistries_List` | `SELECT` | `registryName, resourceGroupName, subscriptionId` | Lists all connected registries for the specified container registry. |
| `ConnectedRegistries_Create` | `INSERT` | `connectedRegistryName, registryName, resourceGroupName, subscriptionId` | Creates a connected registry for a container registry with the specified parameters. |
| `ConnectedRegistries_Delete` | `DELETE` | `connectedRegistryName, registryName, resourceGroupName, subscriptionId` | Deletes a connected registry from a container registry. |
| `ConnectedRegistries_Deactivate` | `EXEC` | `connectedRegistryName, registryName, resourceGroupName, subscriptionId` | Deactivates the connected registry instance. |
| `ConnectedRegistries_Update` | `EXEC` | `connectedRegistryName, registryName, resourceGroupName, subscriptionId` | Updates a connected registry with the specified parameters. |
