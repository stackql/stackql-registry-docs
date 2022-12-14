---
title: move_collections
hide_title: false
hide_table_of_contents: false
keywords:
  - move_collections
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
<tr><td><b>Name</b></td><td><code>move_collections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.resource_mover.move_collections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource Id for the resource. |
| `name` | `string` | The name of the resource |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. |
| `identity` | `object` | Defines the MSI properties of the Move Collection. |
| `location` | `string` | The geo-location where the resource lives. |
| `properties` | `object` | Defines the move collection properties. |
| `tags` | `object` | Resource tags. |
| `etag` | `string` | The etag of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `MoveCollections_Get` | `SELECT` | `api-version, moveCollectionName, resourceGroupName, subscriptionId` | Gets the move collection. |
| `MoveCollections_Create` | `INSERT` | `api-version, moveCollectionName, resourceGroupName, subscriptionId` | Creates or updates a move collection. |
| `MoveCollections_Delete` | `DELETE` | `api-version, moveCollectionName, resourceGroupName, subscriptionId` | Deletes a move collection. |
| `MoveCollections_BulkRemove` | `EXEC` | `api-version, moveCollectionName, resourceGroupName, subscriptionId` | Removes the set of move resources included in the request body from move collection. The orchestration is done by service. To aid the user to prerequisite the operation the client can call operation with validateOnly property set to true. |
| `MoveCollections_Commit` | `EXEC` | `api-version, moveCollectionName, resourceGroupName, subscriptionId, data__moveResources` | Commits the set of resources included in the request body. The commit operation is triggered on the moveResources in the moveState 'CommitPending' or 'CommitFailed', on a successful completion the moveResource moveState do a transition to Committed. To aid the user to prerequisite the operation the client can call operation with validateOnly property set to true. |
| `MoveCollections_Discard` | `EXEC` | `api-version, moveCollectionName, resourceGroupName, subscriptionId, data__moveResources` | Discards the set of resources included in the request body. The discard operation is triggered on the moveResources in the moveState 'CommitPending' or 'DiscardFailed', on a successful completion the moveResource moveState do a transition to MovePending. To aid the user to prerequisite the operation the client can call operation with validateOnly property set to true. |
| `MoveCollections_InitiateMove` | `EXEC` | `api-version, moveCollectionName, resourceGroupName, subscriptionId, data__moveResources` | Moves the set of resources included in the request body. The move operation is triggered after the moveResources are in the moveState 'MovePending' or 'MoveFailed', on a successful completion the moveResource moveState do a transition to CommitPending. To aid the user to prerequisite the operation the client can call operation with validateOnly property set to true. |
| `MoveCollections_ListMoveCollectionsByResourceGroup` | `EXEC` | `api-version, resourceGroupName, subscriptionId` | Get all the Move Collections in the resource group. |
| `MoveCollections_ListMoveCollectionsBySubscription` | `EXEC` | `api-version, subscriptionId` | Get all the Move Collections in the subscription. |
| `MoveCollections_ListRequiredFor` | `EXEC` | `api-version, moveCollectionName, resourceGroupName, sourceId, subscriptionId` | List of the move resources for which an arm resource is required for. |
| `MoveCollections_Prepare` | `EXEC` | `api-version, moveCollectionName, resourceGroupName, subscriptionId, data__moveResources` | Initiates prepare for the set of resources included in the request body. The prepare operation is on the moveResources that are in the moveState 'PreparePending' or 'PrepareFailed', on a successful completion the moveResource moveState do a transition to MovePending. To aid the user to prerequisite the operation the client can call operation with validateOnly property set to true. |
| `MoveCollections_ResolveDependencies` | `EXEC` | `api-version, moveCollectionName, resourceGroupName, subscriptionId` | Computes, resolves and validate the dependencies of the moveResources in the move collection. |
| `MoveCollections_Update` | `EXEC` | `api-version, moveCollectionName, resourceGroupName, subscriptionId` | Updates a move collection. |
