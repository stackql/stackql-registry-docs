---
title: credential_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - credential_sets
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
<tr><td><b>Name</b></td><td><code>credential_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry.credential_sets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed identity for the resource. |
| `properties` | `object` | The properties of a credential set resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `credentialSetName, registryName, resourceGroupName, subscriptionId` | Gets the properties of the specified credential set resource. |
| `list` | `SELECT` | `registryName, resourceGroupName, subscriptionId` | Lists all credential set resources for the specified container registry. |
| `create` | `INSERT` | `credentialSetName, registryName, resourceGroupName, subscriptionId` | Creates a credential set for a container registry with the specified parameters. |
| `delete` | `DELETE` | `credentialSetName, registryName, resourceGroupName, subscriptionId` | Deletes a credential set from a container registry. |
| `_list` | `EXEC` | `registryName, resourceGroupName, subscriptionId` | Lists all credential set resources for the specified container registry. |
| `update` | `EXEC` | `credentialSetName, registryName, resourceGroupName, subscriptionId` | Updates a credential set for a container registry with the specified parameters. |
