---
title: scope_maps
hide_title: false
hide_table_of_contents: false
keywords:
  - scope_maps
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
<tr><td><b>Name</b></td><td><code>scope_maps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry.scope_maps</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `registryName, resourceGroupName, scopeMapName, subscriptionId` | Gets the properties of the specified scope map. |
| `list` | `SELECT` | `registryName, resourceGroupName, subscriptionId` | Lists all the scope maps for the specified container registry. |
| `create` | `INSERT` | `registryName, resourceGroupName, scopeMapName, subscriptionId` | Creates a scope map for a container registry with the specified parameters. |
| `delete` | `DELETE` | `registryName, resourceGroupName, scopeMapName, subscriptionId` | Deletes a scope map from a container registry. |
| `_list` | `EXEC` | `registryName, resourceGroupName, subscriptionId` | Lists all the scope maps for the specified container registry. |
| `update` | `EXEC` | `registryName, resourceGroupName, scopeMapName, subscriptionId` | Updates a scope map with the specified parameters. |
