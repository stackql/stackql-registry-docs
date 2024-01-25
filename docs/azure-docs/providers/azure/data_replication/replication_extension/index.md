---
title: replication_extension
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_extension
  - data_replication
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
<tr><td><b>Name</b></td><td><code>replication_extension</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_replication.replication_extension</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets or sets the Id of the resource. |
| `name` | `string` | Gets or sets the name of the resource. |
| `properties` | `object` | Replication extension model properties. |
| `systemData` | `object` | System data required to be defined for Azure resources. |
| `type` | `string` | Gets or sets the type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `replicationExtensionName, resourceGroupName, subscriptionId, vaultName` | Gets the details of the replication extension. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, vaultName` | Gets the list of replication extensions in the given vault. |
| `create` | `INSERT` | `replicationExtensionName, resourceGroupName, subscriptionId, vaultName, data__properties` | Creates the replication extension in the given vault. |
| `delete` | `DELETE` | `replicationExtensionName, resourceGroupName, subscriptionId, vaultName` | Deletes the replication extension in the given vault. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, vaultName` | Gets the list of replication extensions in the given vault. |
