---
title: pool
hide_title: false
hide_table_of_contents: false
keywords:
  - pool
  - batch
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
<tr><td><b>Name</b></td><td><code>pool</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.batch.pool</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the resource. |
| `name` | `string` | The name of the resource. |
| `properties` | `object` | Pool properties. |
| `type` | `string` | The type of the resource. |
| `etag` | `string` | The ETag of the resource, used for concurrency statements. |
| `identity` | `object` | The identity of the Batch pool, if configured. If the pool identity is updated during update an existing pool, only the new vms which are created after the pool shrinks to 0 will have the updated identities |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Pool_Get` | `SELECT` | `accountName, poolName, resourceGroupName, subscriptionId` | Gets information about the specified pool. |
| `Pool_ListByBatchAccount` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Lists all of the pools in the specified account. |
| `Pool_Create` | `INSERT` | `accountName, poolName, resourceGroupName, subscriptionId` | Creates a new pool inside the specified account. |
| `Pool_Delete` | `DELETE` | `accountName, poolName, resourceGroupName, subscriptionId` | Deletes the specified pool. |
| `Pool_DisableAutoScale` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId` | Disables automatic scaling for a pool. |
| `Pool_StopResize` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId` | This does not restore the pool to its previous state before the resize operation: it only stops any further changes being made, and the pool maintains its current state. After stopping, the pool stabilizes at the number of nodes it was at when the stop operation was done. During the stop operation, the pool allocation state changes first to stopping and then to steady. A resize operation need not be an explicit resize pool request; this API can also be used to halt the initial sizing of the pool when it is created. |
| `Pool_Update` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId` | Updates the properties of an existing pool. |
