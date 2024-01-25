---
title: cache_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - cache_rules
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
<tr><td><b>Name</b></td><td><code>cache_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry.cache_rules</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `cacheRuleName, registryName, resourceGroupName, subscriptionId` | Gets the properties of the specified cache rule resource. |
| `list` | `SELECT` | `registryName, resourceGroupName, subscriptionId` | Lists all cache rule resources for the specified container registry. |
| `create` | `INSERT` | `cacheRuleName, registryName, resourceGroupName, subscriptionId` | Creates a cache rule for a container registry with the specified parameters. |
| `delete` | `DELETE` | `cacheRuleName, registryName, resourceGroupName, subscriptionId` | Deletes a cache rule resource from a container registry. |
| `_list` | `EXEC` | `registryName, resourceGroupName, subscriptionId` | Lists all cache rule resources for the specified container registry. |
| `update` | `EXEC` | `cacheRuleName, registryName, resourceGroupName, subscriptionId` | Updates a cache rule for a container registry with the specified parameters. |
