---
title: archives
hide_title: false
hide_table_of_contents: false
keywords:
  - archives
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
<tr><td><b>Name</b></td><td><code>archives</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry.archives</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `archiveName, packageType, registryName, resourceGroupName, subscriptionId` | Gets the properties of the archive. |
| `list` | `SELECT` | `packageType, registryName, resourceGroupName, subscriptionId` | Lists all archives for the specified container registry and package type. |
| `create` | `INSERT` | `archiveName, packageType, registryName, resourceGroupName, subscriptionId` | Creates a archive for a container registry with the specified parameters. |
| `delete` | `DELETE` | `archiveName, packageType, registryName, resourceGroupName, subscriptionId` | Deletes a archive from a container registry. |
| `_list` | `EXEC` | `packageType, registryName, resourceGroupName, subscriptionId` | Lists all archives for the specified container registry and package type. |
| `update` | `EXEC` | `archiveName, packageType, registryName, resourceGroupName, subscriptionId` | Updates a archive for a container registry with the specified parameters. |
