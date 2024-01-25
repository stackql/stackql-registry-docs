---
title: replicas
hide_title: false
hide_table_of_contents: false
keywords:
  - replicas
  - app_configuration
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
<tr><td><b>Name</b></td><td><code>replicas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_configuration.replicas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the replica. |
| `location` | `string` | The location of the replica. |
| `properties` | `object` | All replica properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `configStoreName, replicaName, resourceGroupName, subscriptionId` | Gets the properties of the specified replica. |
| `list_by_configuration_store` | `SELECT` | `configStoreName, resourceGroupName, subscriptionId` | Lists the replicas for a given configuration store. |
| `create` | `INSERT` | `configStoreName, replicaName, resourceGroupName, subscriptionId` | Creates a replica with the specified parameters. |
| `delete` | `DELETE` | `configStoreName, replicaName, resourceGroupName, subscriptionId` | Deletes a replica. |
| `_list_by_configuration_store` | `EXEC` | `configStoreName, resourceGroupName, subscriptionId` | Lists the replicas for a given configuration store. |
