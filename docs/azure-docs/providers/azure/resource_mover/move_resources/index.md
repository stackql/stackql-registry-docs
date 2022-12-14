---
title: move_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - move_resources
  - resource_mover
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
<tr><td><b>Name</b></td><td><code>move_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.resource_mover.move_resources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource Id for the resource. |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Defines the move resource properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `MoveResources_Get` | `SELECT` | `api-version, moveCollectionName, moveResourceName, resourceGroupName, subscriptionId` | Gets the Move Resource. |
| `MoveResources_List` | `SELECT` | `api-version, moveCollectionName, resourceGroupName, subscriptionId` | Lists the Move Resources in the move collection. |
| `MoveResources_Create` | `INSERT` | `api-version, moveCollectionName, moveResourceName, resourceGroupName, subscriptionId` | Creates or updates a Move Resource in the move collection. |
| `MoveResources_Delete` | `DELETE` | `api-version, moveCollectionName, moveResourceName, resourceGroupName, subscriptionId` | Deletes a Move Resource from the move collection. |
